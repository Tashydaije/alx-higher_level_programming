#!/usr/bin/python3

"""Defines a class - Rectangle"""


class Rectangle:
    """A Rectangle class"""

    """public class attribute"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle

        Args:
            width (int) - width of new rectangle
            height (int) - height of new rectangle
        """

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print rectangle using # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i != self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """deletes an instance of Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Get width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets value of the width of rectangle.

        Args:
            value (int) - value of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets value of the height of the rectangle

        Args:
            value (int) - value of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.height * 2))
