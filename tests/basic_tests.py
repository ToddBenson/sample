"""test the kata exercise"""
from context import add_binary


def test1():
    assert add_binary(1, 1) == "10"


def test2():
    assert add_binary(0, 1) == "1"


def test3():
    assert add_binary(1, 0) == "1"


def test4():
    assert add_binary(2, 2) == "100"


def test5():
    assert add_binary(51, 12) == "111111"
