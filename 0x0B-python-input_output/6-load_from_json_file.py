#!/usr/bin/python3

""" Module to manipulate Object file"""

import json


def load_from_json_file(filename):
    """ creates an obj from a json file

        Args:
            filename (str): path to file
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        obj = json.load(file)
    return obj
