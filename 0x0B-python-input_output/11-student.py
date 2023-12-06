#!/usr/bin/python3

""" Module defines a class Student"""


class Student:
    """ represents a student"""

    def __init__(self, first_name, last_name, age):
        """ Initialization of the instance variables

            Args:
                first_name (str): students first name
                last_name (str): student last name
                age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance

            if attrs is a list of strings, only attr names in list be retrieved
            Otherwise, all attributes must be retrieved

            Args:
                attrs (list): a list of strings
        """
        if (type(attrs) == list and
                all(type(element) == str for elements in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance

            Args:
                json (obj): a dictionary
        """
        for k, v in json.items():
            setattr(self, k, v)
