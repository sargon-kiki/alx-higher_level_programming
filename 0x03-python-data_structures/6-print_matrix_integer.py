#!/usr/bin/python3
# 6-print_matrix_integer.py
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        n_col = ""
        for col in row:
            n_col += "{:d} ".format(col)
        print(n_col)
