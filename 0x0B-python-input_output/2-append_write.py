#!/usr/bin/python3

"""Module for operations on files"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file and
        Returns the number of characters added

        Args:
            filename (str): path to a text file
            text (str): text to append

        Return: number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
