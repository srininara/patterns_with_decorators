def do(operator, arg1, arg2):
    if operator == '+':
        return _add(arg1, arg2)
    elif operator == '-':
        return _subtract(arg1, arg2)
    elif operator == '*':
        return _multiply(arg1, arg2)
    elif operator == '/':
        return _divide(arg1, arg2)
    elif operator == '^':
        return _power(arg1, arg2)
    else:
        raise ValueError('Calc Error - Operator not supported')

def _power(arg1, arg2):
    if arg1 < 1 or arg2 < 1:
        raise ValueError('Calc Error - Natural numbers only supported')
    return arg1 ** arg2

def _divide(arg1, arg2):
    if arg1 < 1 or arg2 < 1:
        raise ValueError('Calc Error - Natural numbers only supported')
    return arg1 / arg2

def _multiply(arg1, arg2):
    if arg1 < 1 or arg2 < 1:
        raise ValueError('Calc Error - Natural numbers only supported')
    return arg1 * arg2

def _subtract(arg1, arg2):
    if arg1 < 1 or arg2 < 1:
        raise ValueError('Calc Error - Natural numbers only supported')
    return arg1 - arg2

def _add(arg1, arg2):
    if arg1 < 1 or arg2 < 1:
        raise ValueError('Calc Error - Natural numbers only supported')
    return arg1 + arg2
