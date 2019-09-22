from app.decorator_utils import only_natural_with_operator
from app.chain import chain_link, pull_chain

def do(operator, arg1, arg2):
    return pull_chain(operator, arg1, arg2)

@chain_link(lambda *args: args[0]=='^')
@only_natural_with_operator
def _power(operator, arg1, arg2):
    return arg1 ** arg2

@chain_link(lambda *args: args[0]=='/')
@only_natural_with_operator
def _divide(operator, arg1, arg2):
    return arg1 / arg2

@chain_link(lambda *args: args[0]=='*')
@only_natural_with_operator
def _multiply(operator, arg1, arg2):
    return arg1 * arg2

@chain_link(lambda *args: args[0]=='-')
@only_natural_with_operator
def _subtract(operator, arg1, arg2):
    return arg1 - arg2

@chain_link(lambda *args: args[0]=='+')
@only_natural_with_operator
def _add(operator, arg1, arg2):
    return arg1 + arg2
