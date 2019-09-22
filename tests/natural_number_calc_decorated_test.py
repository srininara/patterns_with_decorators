# This is the same test as the natural_number_calc_test apart from it working with decorated implementation
# created this so that I can test drive the decorated implementation separately for demo
import pytest

import app.natural_number_calc_decorated as calc


@pytest.mark.parametrize("operator, arg1, arg2, output", [
    ('+',3,2,5),
    ('+',4,2,6),
    ('-',22,12,10),
    ('-',24,4,20),
    ('*',12,7,84),
    ('*',11,11,121),
    ('/',84,6,14),
    ('/',11,11,1),
    ('^',11,2,121),
    ('^',4,3,64),
])
def test_calculator(operator, arg1, arg2, output):
    assert output == calc.do(operator, arg1, arg2)


def test_calculator_operator_not_supported():
    with pytest.raises(ValueError) as ve:
        calc.do('%', 5, 10)

    assert 'Calc Error - Operator not supported' in str(ve.value)


@pytest.mark.parametrize("operator, arg1, arg2", [
    ('+',3,0),
    ('+',4,-2),
    ('-',22,0),
    ('-',-24,4),
    ('*',12,0),
    ('*',11,-4),
    ('/',84,0),
    ('/',12,-2),
    ('^',11,-2),
    ('^',-4,2),
])
def test_calculator_non_natural_numbers_not_supported(operator, arg1, arg2):
    with pytest.raises(ValueError) as ve:
        calc.do(operator, arg1, arg2)

    assert 'Calc Error - Natural numbers only supported' in str(ve.value)
