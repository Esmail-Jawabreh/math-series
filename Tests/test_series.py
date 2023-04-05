import pytest
from Series.series import fibonacci, lucas, sum_series


# Fibonacci Tests

def test_zero_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_one_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_two_fibonacci():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_three_fibonacci():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_four_fibonacci():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_five_fibonacci():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_six_fibonacci():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_seven_fibonacci():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_eight_fibonacci():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_nine_fibonacci():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected


def test_ten_fibonacci():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


# Lucas Tests

def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_two_lucas():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_three_lucas():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_four_lucas():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_five_lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_six_lucas():
    actual = lucas(6)
    expected = 18
    assert actual == expected


def test_seven_lucas():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_eight_lucas():
    actual = lucas(8)
    expected = 47
    assert actual == expected


def test_nine_lucas():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_ten_lucas():
    actual = lucas(10)
    expected = 123
    assert actual == expected


# sum_series Tests

def test_zero_sum_series():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_one_sum_series():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_two_sum_series():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_three_sum_series():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_four_sum_series():
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_five_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_six_sum_series():
    actual = sum_series(6)
    expected = 8
    assert actual == expected


def test_seven_sum_series():
    actual = sum_series(7)
    expected = 13
    assert actual == expected


def test_eight_sum_series():
    actual = sum_series(8)
    expected = 21
    assert actual == expected


def test_nine_sum_series():
    actual = sum_series(9)
    expected = 34
    assert actual == expected


def test_ten_sum_series():
    actual = sum_series(10)
    expected = 55
    assert actual == expected
