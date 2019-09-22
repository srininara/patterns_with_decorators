def only_natural(func):
    def wrapper(arg1, arg2):
        if arg1 < 1 or arg2 < 1:
            raise ValueError('Calc Error - Natural numbers only supported')

        return func(arg1, arg2)
    return wrapper


def only_natural_with_operator(func):
    def wrapper(operator, arg1, arg2):
        if arg1 < 1 or arg2 < 1:
            raise ValueError('Calc Error - Natural numbers only supported')

        return func(operator, arg1, arg2)
    return wrapper


def cor(*, next):
    def wrapper(current):
        def inner(*args):
            output = current(*args)
            return output if output else next(*args) if next else None
        return inner
    return wrapper


def calc_cor(*, my_operator, next=None):
    def wrapper(current):
        def inner(*args):
            if args[0] == my_operator:
                return current(*args)
            elif next:
                return next(*args)
            else:
                raise ValueError('Calc Error - Operator not supported')
        return inner
    return wrapper
