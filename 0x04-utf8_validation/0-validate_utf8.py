#!/usr/bin/python3
""" Script for UTF-8 Validation. """


def validUTF8(data):
    """ Function to determines if a given data set
    represents a valid UTF-8 encoding. """

    num_of_byte = 0

    for byte in data:
        value_of_byte = byte & 255

        if num_of_byte:
            if (value_of_byte >> 6) != 2:
                return False
            num_of_byte -= 1
        else:
            if (value_of_byte >> 7) == 0:
                continue
            elif (value_of_byte >> 5) == 6:
                num_of_byte = 1
            elif (value_of_byte >> 4) == 14:
                num_of_byte = 2
            elif (value_of_byte >> 3) == 30:
                num_of_byte = 3
            else:
                return False

    return num_of_byte == 0
