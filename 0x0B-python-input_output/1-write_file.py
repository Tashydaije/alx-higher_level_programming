#!/usr/bin/python3

"""Module fo functions operating on files"""


def write_file(filename="", text=""):
    """ writes a string to a text file and returns
        number of characters written

        Args:
            filename (str): path to file
            text (str): A text file

        Returns: Number of characters written
    """

    no_of_chars = 0
    with open(filename, mode="w", encoding="utf-8") as file:
        no_of_chars = file.write(text)
    return no_of_chars
