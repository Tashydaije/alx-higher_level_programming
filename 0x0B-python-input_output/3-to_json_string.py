#!/usr/bin/python3

"""Module for operations on files"""

import json


def to_json_string(my_obj):
    """ converts to JSON representation of an obj

        Args:
            my_obj: object to be converted

        Returns:
            string - JSON repn of an obj
    """
    return json.dumps(my_obj)
