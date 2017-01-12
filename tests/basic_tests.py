"""test the kata task"""
from context import pick_peaks


def test8():
    assert pick_peaks([1,2,2,2,3]) == {"pos": [], "peaks": []}


def test5():
    assert pick_peaks([2,1,3,1,2,2,2,2]) == {"pos": [2], "peaks": [3]}


def test1():
    assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos": [3,7], "peaks": [6,3]}


def test2():
    assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]) == {"pos": [3,7], "peaks": [6,3]}


def test3():
    assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos": [3,7,10], "peaks": [6,3,2]}


def test4():
    assert pick_peaks([2,1,3,1,2,2,2,2,1]) == {"pos": [2,4], "peaks": [3,2]}


def test6():
    assert pick_peaks([1,1,1,1,1,1,1,1]) == {"pos": [], "peaks": []}


def test7():
    assert pick_peaks([1,2,2,2,2,2,2,1]) == {"pos": [1], "peaks": [2]}
