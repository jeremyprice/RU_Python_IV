import dis


def myFunc():
    x = 1
    y = 2
    z = 'abc'  # noqa
    return x + y

print myFunc.func_name
print myFunc.func_code.co_varnames
print myFunc.func_code.co_consts
print myFunc.func_code.co_code

dis.disassemble(myFunc.func_code)
