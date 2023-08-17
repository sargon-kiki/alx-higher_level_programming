#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    """Calc square matrix"""
    final = [list(map(lambda x: x**2, row)) for row in matrix]
    return final
