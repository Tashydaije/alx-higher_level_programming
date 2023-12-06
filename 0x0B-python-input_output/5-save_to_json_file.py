#!/usr/bin/python3

"""Module for writing object to text file"""

import json


def save_to_json_file(my_obj, filename):
    """ Writes obj to text file using json repn

        Args:
            my_obj: an object
            filename (str): file path

        Returns:
            None
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        obj_json = json.dumps(my_obj)
        file.write(obj_json)
