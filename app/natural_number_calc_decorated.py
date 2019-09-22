from app.decorator_utils import only_natural

def do(operator, arg1, arg2):
    if operator == '+':
        return _add(arg1, arg2)
    elif operator == '-':
        return _subtract(arg1, arg2)
    elif operator == '*':
        return _multiply(arg1, arg2)
    elif operator == '/':
        return divide(arg1, arg2)
    elif operator == '^':
        return _power(arg1, arg2)
    else:
        raise ValueError('Calc Error - Operator not supported')

@only_natural
def _power(arg1, arg2):
    return arg1 ** arg2

@only_natural
def divide(arg1, arg2):
    return arg1 / arg2

@only_natural
def _multiply(arg1, arg2):
    return arg1 * arg2

@only_natural
def _subtract(arg1, arg2):
    return arg1 - arg2

@only_natural
def _add(arg1, arg2):
    return arg1 + arg2