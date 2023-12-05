#!/usr/bin/python3

"""Module contains functions that operate on files"""


def read_file(filename=""):
    """Reads a text file

        Args:
            filename (str): file nmae with .txt extn
    """
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
