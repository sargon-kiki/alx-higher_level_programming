#!/usr/bin/python3
# 3-safe_print_division.py


def safe_print_division(a, b):
    """Safe print division"""
    div_result = None
    try:
        div_result = a / b
    except (ZeroDivisionError, TypeError):
        div_result = None
    finally:
        print("Inside result: {}".format(div_result))
    return div_result
