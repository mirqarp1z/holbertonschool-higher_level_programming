#!/usr/bin/python3
"""Abstract Animal class and its subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method that should be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog subclass of Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass of Animal"""

    def sound(self):
        return "Meow" 
