"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



while True:
    inp_string = input('Enter your expression: ')
    tokens = inp_string.split(' ')
    result = None
    num1 = tokens[1]
    num2 = tokens[2]
    
    for token in tokens:
        if token == 'q':
            print("Goodbye.")
            break
    if len(tokens) < 2:
        num2 = 0

    
    if tokens[0] == '+':
        result = add(float(num1), float(num2))
    elif tokens[0] == '-':
        result = subtract(float(num1), float(num2))
    elif tokens[0] == '*':
        result = multiply(float(num1), float(num2))
    elif tokens[0] == '/':
        result = divide(float(num1), float(num2))
    elif tokens[0] == 'square':
        result = square(float(num1))
    elif tokens[0] == 'cube':
        result = cube(float(num1))
    elif tokens[0] == 'pow':
        result = power(float(num1), float(num2))
    elif tokens[0] == 'mod':
        result = mod(float(num1), float(num2))
    print(result)




