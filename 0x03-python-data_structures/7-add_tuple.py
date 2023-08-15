#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples together."""
    maze_a = tuple_a + (0, 0)
    maze_b = tuple_b + (0, 0)
    first = maze_a[0] + maze_b[0]
    second = maze_b[1] + maze_a[1]
    return (first, second)
