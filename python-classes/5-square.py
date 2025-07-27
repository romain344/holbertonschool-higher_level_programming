#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """represent a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """get the size of the square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        def area(self):
            return self.__size ** 2
        
    def my_print(self):
        """Print the square with the character """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
