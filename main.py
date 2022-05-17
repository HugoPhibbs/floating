# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def ibm_single_to_double_exponant(binary):
    binary_to_decimal("1000010")


def ibm_single_to_single_fraction(binary):
    sign_bit = binary[0:1]
    sign = 0
    if sign_bit == '1':
        sign = -1
    else:
        sign = 1

    #convert exponant binary to decimal value
    exponant_binary = binary[1:8]
    exponant = binary_to_decimal(exponant_binary)


    #convert binary fraction
    fraction_binary = binary[8:len(binary)]
    hexi = hex(int(fraction_binary, 2))
    find_index = hexi.index("x")
    start = hexi[0:find_index] #this is what changed if broken
    middle = "0."
    end = hexi[2:len(hexi)]
    fraction_hex = start + middle + end
    fraction = float.fromhex(fraction_hex)
    ibm_to_float_math_single(sign,exponant,fraction)


def ibm_to_float_math_single(sign, exponant, fraction):
    convert = pow(sign,1) * fraction * pow(16,exponant-64);
    print(convert)



def binary_to_decimal(binary):
    binary = ''.join(reversed(binary))
    decimal = 0
    for i in range(0, len(binary)):
        decimal += int(binary[i])*2**i
    return decimal




if __name__ == '__main__':
    ibm_single_to_single_fraction("0000000000001111111111111111111111111111111111111111111111111111")
    #dec = float.fromhex("0x0.76A000")
    #binary_to_decimal("1000010")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/




