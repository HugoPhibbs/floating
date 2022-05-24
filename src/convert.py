import struct
import binascii


class Convert:
    """
    Main logical class of the Project, does conversion from IBM floating points to IEEE floating points
    """


    # Main Methods

    def start(self) -> None:
        """
        Starts the convert program. Main method for this application

        :return: None
        """
        input_file_name = self.get_input_file_name()

        output_file_name = self.get_output_file_name()
        float_list = self.convert_ibm_file(input_file_name)
        ieee_list = []
        for float in float_list:
            ieee_list.append(self.float_to_ieee(float))



        self.write_to_ieee_file(ieee_list, output_file_name)

    def convert_ibm_file(self, file_name: str):
        """
        Converts a file containing IBM binary float to a list of IEEE floats

        :param file_name: str name of file containing IBM binary floats to be converted
        :param input_format: str format of inputted ibm file content
        :return: list containing IBM floats converted into python floats
        """

        byte_content = self.read_bin_file(file_name)
        return self.ibm_bytes_to_float_list(byte_content)

    # Converting ibm to float

    def ibm_bytes_to_float_list(self, byte_content: bytes) -> list:
        """
        Converts IBM byte content of a specified format and converts the file into a list
        of python floats

        The way we read in removes the leading zero as it thinks its padding, so
        I append any necessary zeros according to inputted format

        Handles parsing byte content according to format size.

        :param byte_content: bytes for content read from a binary file
        :param input_format: string for input format of the ibm byte_content
        :return: list of floats as described
        """

        increment: int = 8

        binary_int = binascii.hexlify(byte_content)
        binary_string = binary_int[0:len(binary_int)]

        float_list = []
        x = 0

        while x < len(binary_string):
            bin_string = binary_string[x:x + increment]

            storage = (hex(int(bin_string, 16)))
            storage1 = (bin(int(storage, 16)))
            storage1 = storage1[2:len(storage1)]
            if (len(storage1) == 31):
                storage1 = "0" + storage1

            this_float = self.ibm_to_float(storage1)
            float_list.append(this_float)
            x += increment
        return float_list

    def ibm_to_float(self, ibm_binary: str) -> float:
        """
        Converts an IBM binary bit pattern given into a float

        :param ibm_binary str for inputted binary IBM float from a user
        :return: float for inputted IBM binary string
        """

        # Getting sign of binary
        sign_bit = ibm_binary[0]
        sign = 1 if sign_bit == "1" else -1

        # convert exponent binary to decimal value
        exponent_binary = ibm_binary[1:8]
        exponent = self.binary_to_decimal(exponent_binary)

        # convert binary fraction
        fraction_binary = ibm_binary[8:len(ibm_binary)]
        hexi = hex(int(fraction_binary, 2))
        find_index = hexi.index("x")
        start = hexi[0:find_index]  # this is what changed if broken
        middle = "0."
        end = hexi[2:len(hexi)]
        fraction_hex = start + middle + end
        fraction = float.fromhex(fraction_hex)

        return self.ibm_to_float_equation(sign, exponent, fraction)

    def ibm_to_float_equation(self, sign, exponent, fraction) -> float:
        """
        Takes the decimal exponent and hexi-decimal fraction and converts to the float.

        :param exponent: decimal value of the binary transformed in previous method.
        :param fraction: hexi-decimal value of the binary transformed in previous method.
        :return: float
        """
        return pow(sign, 1) * fraction * pow(16, exponent - 64)

    def binary_to_decimal(self, binary) -> float:
        """
        Converts binary to decimal

        :return: decimal float
        """
        binary = ''.join(reversed(binary))
        decimal = 0
        for i in range(0, len(binary)):
            decimal += int(binary[i]) * 2 ** i
        return decimal

    # Converting float to IEEE

    def float_to_ieee(self, num: float) -> str:
        """
        Converts a float number into an IEEE single precision binary string

        code taken from https://stackoverflow.com/questions/51179116/ieee-754-python

        :param num: float for float to be converted
        :param output_format: string for format of ieee float to use, either "single or double"
        :return: string for IEEE binary as described
        """

        bits, = struct.unpack('!I', struct.pack('!f', num))

        return "{:032b}".format(bits)


    # Handling input and output

    def write_to_ieee_file(self, float_list: list, output_file_name: str) -> None:
        """
        Writes a list of converted IBM floats to a file containing IEEE floats

        :param float_list: list of floats to be written to IEEE
        :param output_file_name: str for name of file to be written to
        :return: None
        """

        ieee_binary_list = []
        for float in float_list:
            ieee_binary_list.append(float)
        ## TODO write to file

        f = open(output_file_name, "wb")
        for element in ieee_binary_list:
            f.write(element.encode('utf-8'))

        f.close
        print("See newly created file.")


    def get_input_file_name(self) -> str:
        """
        Gets name for the IBM input file

        :return: str
        """
        return input("Please enter the directory of an input file: ")

    def get_output_file_name(self) -> str:
        """
        Gets name for the IEEE output file

        :return: str
        """
        return input("Please enter the directory of an output file: ")

    def read_bin_file(self, file_name: str) -> bytes:
        """
        Reads an inputted binary file from a user, and returns the content to a user

        :param file_name: str for name of binary file to be opened
        :return:
        """
        return open(file_name, "rb").read()



# print(len("1000000000000000000000000000000000000000000000000000000000000000"))
# binary_string = binascii.hexlify("804E28E2290F0000")
# print(binary_string)
# Convert().read_file_and_call_conversion_single("../test/test_files/testIBMSingle(1).bin")
# Convert().input_sequence()
# Convert().read_file_and_call_conversion()
Convert().start()
