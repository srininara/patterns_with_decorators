def only_natural(func):
    def wrapper(arg1, arg2):
        if arg1 < 1 or arg2 < 1:
            raise ValueError('Calc Error - Natural numbers only supported')

        return func(arg1, arg2)
    return wrapper
