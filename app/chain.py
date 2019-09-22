CHAINED = []

def chain_link(predicate):
    def wrapper(action):
        CHAINED.append((predicate,action))
        return action
    return wrapper


def pull_chain(*args):
    for predicate,action in CHAINED:
        if predicate(*args):
            return action(*args)

    raise ValueError('Calc Error - Operator not supported')
