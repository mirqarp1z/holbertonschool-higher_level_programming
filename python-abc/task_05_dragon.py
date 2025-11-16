#!/usr/bin/python3
"""Mixins example with Dragon"""


class SwimMixin:
    """Mixin that adds swimming capability"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying capability"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar"""

    def roar(self):
        print("The dragon roars!")
