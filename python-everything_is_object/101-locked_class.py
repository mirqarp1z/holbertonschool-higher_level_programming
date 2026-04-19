#!/usr/bin/python3
"""Defines a locked class that only allows first_name attribute."""

class LockedClass:
    __slots__ = ("first_name",)

