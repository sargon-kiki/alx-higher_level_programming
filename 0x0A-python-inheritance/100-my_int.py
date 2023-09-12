#!/usr/bin/python3
# 100-my_int.py

"""Defined an inherit of int class"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Ops overload == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Ops overload != operator with == behavior."""
        return self.real == value
