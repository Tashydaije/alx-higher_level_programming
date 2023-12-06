#!/usr/bin/python3

""" Defines a class Student """


class Student:
    """ Represents a student """

    def __init__(self, first_name, last_name, age):
        """ Initialization of the instance variables

            Args:
                first_name (str): students first name
                last_name (str): students last name
                age (int): students age
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
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
