#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A function that computes the square value. Use Map and Lambda"""
    return list(map(lambda x: list(map(lambda x : x**x,y )), matrix))
