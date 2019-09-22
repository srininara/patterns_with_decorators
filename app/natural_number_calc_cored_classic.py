from app.decorator_utils import only_natural_with_operator, cor

def do(operator, arg1, arg2):
    value = _add(operator, arg1, arg2)
    if value:
        return value
    else:
        raise ValueError('Calc Error - Operator not supported')

@only_natural_with_operator
def _power(operator, arg1, arg2):
    if operator == '^':
        return arg1 ** arg2
    else:
        return None

@only_natural_with_operator
@cor(next=_power)
def _divide(operator, arg1, arg2):
    if operator == '/':
        return arg1 / arg2
    else:
        return None

@only_natural_with_operator
@cor(next=_divide)
def _multiply(operator, arg1, arg2):
    if operator == '*':
        return arg1 * arg2
    else:
        return None

@only_natural_with_operator
@cor(next=_multiply)
def _subtract(operator, arg1, arg2):
    if operator == '-':
        return arg1 - arg2
    else:
        return None

@only_natural_with_operator
@cor(next=_subtract)
def _add(operator, arg1, arg2):
    if operator == '+':
        return arg1 + arg2
    else:
        return None
