import pytest

from day_6 import process_input


def test_input():
    value = """abc

    a
    b
    c"""
    result = process_input(value)
    assert list(map(list, result)) == [[{"a", "b", "c"}], [{"a"}, {"b"}, {"c"}]]
