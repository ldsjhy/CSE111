"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix, compute_area, compute_square_root
import pytest
from pytest import approx


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"


def test_suffix():
    """Verify that the suffix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    # function_output = prefix("hilarious", "nefarious")
    # assert isinstance(function_output, str), "suffix function must return a string"
    assert suffix("hilarious", "nefarious") == "arious"
    assert suffix("hilarious", "nefarious") == "arioussasaas"

def test_compute_area():
    assert compute_area(5, 10) == 50
    assert compute_area(200, 10) == 2000
    assert compute_area(.5, 10) == 50

def test_compute_square_root():
    assert compute_square_root(5) == approx(2.2361, 0,0001)
    # assert compute_square_root(5) == 2.24

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
