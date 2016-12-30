"""test the kata exercise"""
from context import is_square
import random


def test1():
    assert is_square(-1) is False


def test():
    assert is_square(3) is False


def test2():
    assert is_square(4) is True


def test3():
    assert is_square(25) is True


def test4():
    assert is_square(26) is False
