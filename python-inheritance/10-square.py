#!/usr/bin/python3
"""Module doc."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        name = self.__class__.__name__
        return f"[{name}] {self.__width}/{self.__height}"
