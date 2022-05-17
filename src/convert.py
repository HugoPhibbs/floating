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

Convert().get_input()