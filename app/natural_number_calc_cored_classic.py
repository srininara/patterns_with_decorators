from app.decorator_utils import only_natural_with_operator, calc_cor

def do(operator, arg1, arg2):
    return _add(operator, arg1, arg2)

@only_natural_with_operator
@calc_cor(my_operator='^')
def _power(operator, arg1, arg2):
    return arg1 ** arg2

@only_natural_with_operator
@calc_cor(my_operator='/', next=_power)
def _divide(operator, arg1, arg2):
    return arg1 / arg2

@only_natural_with_operator
@calc_cor(my_operator='*', next=_divide)
def _multiply(operator, arg1, arg2):
    return arg1 * arg2

@only_natural_with_operator
@calc_cor(my_operator='-', next=_multiply)
def _subtract(operator, arg1, arg2):
    return arg1 - arg2

@only_natural_with_operator
@calc_cor(my_operator='+', next=_subtract)
def _add(operator, arg1, arg2):
    return arg1 + arg2
