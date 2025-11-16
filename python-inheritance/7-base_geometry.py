#!/usr/bin/python3
"""Defines a Geometry class."""


class BaseGeometry:
    """
    Represents a  Geometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
