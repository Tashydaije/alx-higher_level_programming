#!/usr/bin/python3

""" Module for operations on files"""

import json


def from_json_string(my_str):
    """ Deserialization - returns object repd by JSON string

        Args:
            my_str: JSON repn(string)

        Returns:
            An object
    """

    return json.loads(my_str)
