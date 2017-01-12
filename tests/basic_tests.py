"""test the kata task"""
from context import maxSequence


def test1():
    assert maxSequence([]) == 0


def test2():
    assert maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test3():
    assert maxSequence([1, 2, -4, 3, -7, 8, 9]) == 17


def test4():
    assert maxSequence([1, 2, 3, 4, 5, 1]) == 16

# [-1] [-1, 3] [-1, 3, 4] [-1, 3, 4, 5]
# [3] [3, 4] [3, 4, 5]
# [4] [4, 5]
# [5]


def test5():
    assert maxSequence([-1, 3, 4, 5]) == 12


def test6():
    assert maxSequence([-1, -3, -4, -5]) == 0


def test7():
    assert maxSequence([1, 3, 4, -5]) == 8
