#!/usr/bin/python3


if __name__ == "__main__":
    """Print the formats from functions imported from calc.py"""
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
