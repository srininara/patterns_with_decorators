CHAIN = []

def link_to_chain(predicate):
    def wrapper(operator):
        CHAIN.append((predicate,operator))
        return operator
    return wrapper


def pull_chain(*args):
    for predicate,operator in CHAIN:
        if predicate(*args):
            return operator(*args)

    raise ValueError('Calc Error - Operator not supported')
