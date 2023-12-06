#!/usr/bin/python3

""" Defines a class-to-json function
"""


def class_to_json(obj):
    """ Returns the dictionary descriptionnwith simple DS
        for JSON serialization of an object
    """
    return obj.__dict__
