#!/usr/bin/python3

""" Module that defines a class - Student
"""


class Student:
    """ A class repn a Student """

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

    def to_json(self):
        """ Retrieves a dictionary represanation of a student instance
        """
        return self.__dict__
