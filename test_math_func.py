import pytest
import math_func

@pytest.mark.number
def test_add():
  assert math_func.add(7, 3) == 10
  assert math_func.add(7) == 9
  assert math_func.add(-2) == 0

@pytest.mark.number
def test_product():
  assert math_func.product(5, 5) == 25
  assert math_func.product(5) == 10
  assert math_func.product(-5) == -10
  assert math_func.product(2) != 7

@pytest.mark.strings
def test_add_strings():
  result = math_func.add('Hello', ' World')
  assert result == 'Hello World'
  assert type(result) is str
  assert 'Orange' not in result

@pytest.mark.strings
def test_product_strings():
  assert math_func.product('Yadda ', 3) == 'Yadda Yadda Yadda '
  result = math_func.product('Yadda ')
  assert result == 'Yadda Yadda '
  assert type(result) is str
  assert 'Ya' in result

if __name__ == '__main__':
  pytest.main()
  # or in terminal run py.test -v