"""Add two numbers together and convert to binary"""
import math


def is_square(integer):
    """Calculate the sqrt"""
    if integer < 1:
        return False
    root = math.sqrt(integer)
    return int(root + 0.5) ** 2 == integer
