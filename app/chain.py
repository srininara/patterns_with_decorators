CHAINED = []

def chain_link(my_operator):
    def wrapper(func):
        CHAINED.append((my_operator,func))
        return func
    return wrapper


def pull_chain(*args):
    for my_operator,func in CHAINED:
        if my_operator == args[0]:
            return func(*args)

    raise ValueError('Calc Error - Operator not supported')
