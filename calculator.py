"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



while True:
    inp_string = input('Enter your expression: ')
    tokens = inp_string.split(' ')
    
    for token in tokens:
        if token == 'q':
            print("Goodbye.")
            break
    if len(tokens) < 3:
        input("Please enter your prefix followed by two integers:")

    result = None
    num1 = tokens[1]
    num2 = tokens[2]

    
    if tokens[0] == '+':
        result = add(float(num1), float(num2))
    elif tokens[0] == '-':
        result = subtract(num1, num2)
    elif tokens[0] == '*':
        result = multiply(num1, num2)
    elif tokens[0] == '/':
        result = divide(num1, num2)
    elif tokens[0] == 'square':
        result = square(num1)
    elif tokens[0] == 'cube':
        result = cube(num1)
    elif tokens[0] == 'pow':
        result = power(num1, num2)
    elif tokens[0] == 'mod':
        result = mod(num1, num2)
    print(result)




