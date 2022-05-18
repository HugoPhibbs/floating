import struct


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
        print(content.decode(encoding="CP500"))

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




    def ibm_to_float(binary):
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
        exponant = binary_to_decimal(exponant_binary)

        # convert binary fraction
        fraction_binary = binary[8:len(binary)]
        hexi = hex(int(fraction_binary, 2))
        find_index = hexi.index("x")
        start = hexi[0:find_index]  # this is what changed if broken
        middle = "0."
        end = hexi[2:len(hexi)]
        fraction_hex = start + middle + end
        fraction = float.fromhex(fraction_hex)
        ibm_to_float_math_single(sign, exponant, fraction)

    def ibm_to_float_math_single(sign, exponant, fraction):
        """
        takes the decimal exponant and hexidecimal fraction and converts
        to the float.
        :param exponant: deciaml value of the binary transformed in previous method.
        :param fraction: hexidecimal value of the binary transformed in previous method.
        :return: float
        """
        convert = pow(sign, 1) * fraction * pow(16, exponant - 64);
        print(convert)

    def binary_to_decimal(binary):
        """
        converts binary to decimal
        :return: decimal
        """
        binary = ''.join(reversed(binary))
        decimal = 0
        for i in range(0, len(binary)):
            decimal += int(binary[i]) * 2 ** i
        return decimal

    if __name__ == '__main__':
        ibm_to_float("11000010011101101010000000000000")
        ibm_to_float("01111111111111111111111111111111")
        ibm_to_float("00000000000100000000000000000000")
        # dec = float.fromhex("0x0.76A000")
        # binary_to_decimal("1000010")


Convert().get_input()