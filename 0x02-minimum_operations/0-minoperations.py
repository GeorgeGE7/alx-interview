#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    number_of_chars = 1
    number_of_copies = 0
    operations_counter = 0

    while number_of_chars < n:
        if number_of_copies == 0:
            number_of_copies = number_of_chars
            operations_counter += 1

        if number_of_chars == 1:
            number_of_chars += number_of_copies
            operations_counter += 1
            continue

        remaining = n - number_of_chars
        if remaining < number_of_copies:
            return 0

        if remaining % number_of_chars != 0:
            number_of_chars += number_of_copies
            operations_counter += 1
        else:
            number_of_copies = number_of_chars
            number_of_chars += number_of_copies
            operations_counter += 2

    if number_of_chars == n:
        return operations_counter
    else:
        return 0
