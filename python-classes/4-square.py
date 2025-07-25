#!/usr/bin/python3
"""define la class"""


class Square:
    """class square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """getter of size"""
        return  self.__size

    @size.setter
    def size(self, value):
        """setter of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2
