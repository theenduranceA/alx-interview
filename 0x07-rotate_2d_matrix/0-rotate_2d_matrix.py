#!/usr/bin/python3
""" Script for 2D Matrix."""


def rotate_2d_matrix(matrix):
    """ Function for a 2D Matrix rotated at 90° """

    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i],  matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
