import pytest
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from calcs import square, double, first_name

@pytest.fixture
def create_example_name():
    first = 'Jim'
    last = 'Smith'
    full = f'{first} {last}'
    return first, full

def test_first_name(create_example_name):
    assert first_name(create_example_name[1]) == create_example_name[0]

def test_square():
    assert square(3) == 9
    assert square(-5) == 25
    assert square(0) == 0

def test_double():
    assert double(3) == 6
    assert double(-5) == -10
    assert double(0) == 0

