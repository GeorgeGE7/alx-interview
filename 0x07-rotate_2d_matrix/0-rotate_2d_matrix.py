#!/usr/bin/python3
"""
Matrix (2D) Rotation
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Rotates arrays - 2d matrix
    """
    m_range = int(len(matrix) / 2)
    for m in range(m_range):
        for n in range(m, (len(matrix) - m - 1)):
            x = (len(matrix) - 1 - n)
            tmp = matrix[m][n]
            matrix[m][n] = matrix[x][m]
            matrix[x][m] = matrix[(len(matrix) - m - 1)][x]
            matrix[(len(matrix) - m - 1)][x] = matrix[n][(len(matrix) - m - 1)]
            matrix[n][(len(matrix) - m - 1)] = tmp
