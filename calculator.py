"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

run = True

while run:
    inp_string = input('Enter your expression: ')
    tokens = inp_string.split(' ')

    for token in tokens:
        if token == 'q':
            run = False
            print("Goodbye.")
            break
        elif len(tokens) < 3:
            input("Please enter your prefix followed by two integers:")
    
    if tokens[0] == '+':
        result = add(token[1], token[2])
