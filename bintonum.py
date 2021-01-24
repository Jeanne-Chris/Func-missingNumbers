""" A simple function that converts binary strings to regular integers."""


def bintoint(binary_string):

    if binary_string.replace('0', '').replace('1', ''):
        return False, 'Input string contains INVALID character, binary is 0 and 1.'

    convert_num = 0

    for char in binary_string:
        convert_num *= 2
        convert_num += int(char)
    convert_mess = binary_string + ' is equivalent to '

    return convert_mess + str(convert_num)


bin_str = input("\nEnter BINARY STRING to interpret : ")
print(bintoint(bin_str))
