#!/usr/bin/python3
"""module doc"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
