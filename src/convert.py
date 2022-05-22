import struct
import binascii


class Convert:
    """
    Main logical class of the Project, does conversion from IBM floating points to IEEE floating points
    """
    sizes = ["double", "single"]

    def get_input(self) -> str:
        """
        Gets file input from a user

        :return:
        """
        file_reader = open(input("Please enter the directory of an input file: "), "rb")
        content = file_reader.read()
        print(content.decode(encoding="cp1140"))

        print(codecs.decode(content, "hex"))

    def read_bin_file(self, file_name : str):
        """
        Reads an inputted binary file from a user, and returns the content to a user

        :param file_name: str for name of binary file to be opened
        :return:
        """
        return open(file_name, "rb").read()


    def get_output_format(self):
        """
        Gets the output (single or double) that a user would like the IBM floats to be converted to

        :return: str for
        """
        pass

    def convert(self, ibm_binary: str, size : str) -> str:
        """
        Converts an IBM binary float to IEEE float

        :param ibm_binary: str for IBM binary float to be converted
        :param size: str for size of IEEE float to be converted to
        :return: str for binary form of IEEE float
        """
        assert size in self.sizes
        return ""  # TODO

    def ibm_to_float(self, ibm_binary : str) -> float:
        """
        Converts an IBM binary float to a python float
        :param ibm_binary:
        :return:
        """
        pass # TODO

    def float_to_ieee(self, num : float, size : str) -> str:
        """
        Converts a float number into an IEEE single precision binary string

        code taken from https://stackoverflow.com/questions/51179116/ieee-754-python

        :param num: float for float to be converted
        :param size: string for size of ieee float to use, either "single or double"
        :return: string for IEEE binary as described
        """
        assert size in self.sizes
        bits, = struct.unpack('!I', struct.pack('!f', num))
        if size == "single":
            return "{:032b}".format(bits)
        else:
            return "{:064b}".format(bits)




    def ibm_to_float(self, binary):
        """
        converts the bitpattern given into a float from ibm
        :return: the float version of the binary ibm
        """
        sign_bit = binary[0:1]
        sign = 0
        if sign_bit == '1':
            sign = -1
        else:
            sign = 1

        # convert exponant binary to decimal value
        exponant_binary = binary[1:8]
        exponant = Convert().binary_to_decimal(exponant_binary)

        # convert binary fraction
        fraction_binary = binary[8:len(binary)]
        hexi = hex(int(fraction_binary, 2))
        find_index = hexi.index("x")
        start = hexi[0:find_index]  # this is what changed if broken
        middle = "0."
        end = hexi[2:len(hexi)]
        fraction_hex = start + middle + end
        fraction = float.fromhex(fraction_hex)
        Convert().ibm_to_float_math_single(sign, exponant, fraction)

    def ibm_to_float_math_single(self ,sign, exponant, fraction):
        """
        takes the decimal exponant and hexidecimal fraction and converts
        to the float.
        :param exponant: deciaml value of the binary transformed in previous method.
        :param fraction: hexidecimal value of the binary transformed in previous method.
        :return: float
        """
        convert = pow(sign, 1) * fraction * pow(16, exponant - 64);
        print(convert)

    def binary_to_decimal(self, binary):
        """
        converts binary to decimal
        :return: decimal
        """
        binary = ''.join(reversed(binary))
        decimal = 0
        for i in range(0, len(binary)):
            decimal += int(binary[i]) * 2 ** i
        return decimal




    def read_file_and_call_conversion_single(self,file):
        """
        reads in the file (this needs to be changed so it takes a file and a type
        Single or double).
        the way we read in removes the leading zero as it thinks its padding, so
        i append that if length 31 or 63
        need to adjust this method so it works for both 32 and 64 as it only works for
        32 at the moment.
        :return:
        """

        file_reader = open(file, "rb")
        content = file_reader.read()
        binary_int = binascii.hexlify(content)
        binary_string = binary_int[0:len(binary_int)]
        x = 0
        while x < len(binary_string):
            bin_string = binary_string[x:x + 8]

            storage = (hex(int(bin_string, 16)))
            storage1 = (bin(int(storage, 16)))
            storage1 = storage1[2:len(storage1)]
            if (len(storage1) == 31 or len(storage1) == 63):
                    storage1 = "0" + storage1

            Convert().ibm_to_float(storage1)
            x+= 8

    def read_file_and_call_conversion_double(self,file):
        """
        reads in the file (this needs to be changed so it takes a file and a type
        Single or double).
        the way we read in removes the leading zero as it thinks its padding, so
        i append that if length 31 or 63
        need to adjust this method so it works for both 32 and 64 as it only works for
        32 at the moment.
        :return:
        """

        file_reader = open(file, "rb")
        content = file_reader.read()
        binary_int = binascii.hexlify(content)
        binary_string = binary_int[0:len(binary_int)]
        x = 0
        while x < len(binary_string):
            bin_string = binary_string[x:x + 16]

            storage = (hex(int(bin_string, 16)))
            storage1 = (bin(int(storage, 16)))
            storage1 = storage1[2:len(storage1)]
            if (len(storage1) == 31 or len(storage1) == 63):
                storage1 = "0" + storage1

            Convert().ibm_to_float(storage1)
            x += 16


    def get_input_type(self):
        """
        gets the persiscion type
        :return: string of what percsision
        """
        val = input("Enter percision (double or Single): ")
        return val

    def get_file(self):
        """
        gets the file path
        :return: String file path
        """
        val = input("Enter file to read from")
        return val


    def read_file(self, percision, file):
        """
        reads the file with the specified percsion
        :param self:
        :param percision: double or single
        :param file: the file to read from
        :return: nothing
        """

        if(percision == "single"):

            Convert().read_file_and_call_conversion_single(file)

        elif(percision == "double"):

            Convert().read_file_and_call_conversion_double(file)

        else:
            print("percision not recoginised")

    def input_sequence(self):
        """
        called to run the program in the correct sequence
        :return: nothing
        """
        file = Convert().get_file()
        percision = Convert().get_input_type()
        Convert().read_file(percision,file)




#print(len("1000000000000000000000000000000000000000000000000000000000000000"))
#binary_string = binascii.hexlify("804E28E2290F0000")
#print(binary_string)
Convert().read_file_and_call_conversion_single("../test/test_files/testIBMSingle.bin")
#Convert().input_sequence()
#Convert().read_file_and_call_conversion()



