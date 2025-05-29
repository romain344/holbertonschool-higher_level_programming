#!/usr/bin/python3
""" Rectangle class definition with area method """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


rectangle = __import__('8-rectangle').Rectangle
class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self .integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        area  = rectangle.__width * rectangle.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    