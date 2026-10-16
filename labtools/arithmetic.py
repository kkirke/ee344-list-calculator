import numpy as np

"""Calculate a sum or product from a list of numbers."""


def add(numbers):
    """Return the sum of the numbers; an empty list has sum 0."""
    total = 0
    for number in numbers:
        total = total + number
    return total


def multiply(numbers):
    """Return the product of the numbers; an empty list has product 1."""
    # Assignment 1: replace this line with an implementation using a for loop.
    total = 1
    for number in numbers:
        total = total * number
    return total

def add_numpy(numbers):
    return np.sum(numbers)

def multiply_numpy(numbers):
    return np.prod(numbers)
