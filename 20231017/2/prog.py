from math import *

dictionary = {}
functions = 1
strings = 1
while (s := input()).split()[0] != 'quit':
    strings += 1
    if s[0] == ':':
        func_name, *args, expr = s.split()
        func_name = func_name[1:]
        functions += func_name not in dictionary
        dictionary[func_name] = (args, expr, len(args) == 1)
    else:
        if ' ' not in s:
            func_name = s
        else:
            func_name = s[:s.index(' ')]
            if dictionary[func_name][2]:
                args = [s[s.index(' ') + 1:]]
            else:
                func_name, *args = s.split()
        args_letters, expr, tmp  = dictionary[func_name]
        for i in range(len(args)):
            exec(f"{args_letters[i]} = {args[i]}")
        exec(f'print({expr})')
exec(f"print({s[s.index('quit') + 4:]}.format(functions, strings))")
