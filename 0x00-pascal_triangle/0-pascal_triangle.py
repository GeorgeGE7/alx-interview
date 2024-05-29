#!/usr/bin/python3
"""Create a pascal's triangle for n"""


def pascal_triangle(n):
    """
    returns a list of lists of integers for  n
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        second_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                second_list.append(1)
            else:
                second_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(second_list)
    return triangle
