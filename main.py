# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def binary_to_decimal(binary):
    binary = ''.join(reversed(binary))
    decimal = 0
    for i in range(0, len(binary)):
        decimal += int(binary[i])*2**i
    print("The decimal value is:", decimal)



def ibm_single_to_single():


if __name__ == '__main__':
    binary_to_decimal("11101101010000000000000")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




