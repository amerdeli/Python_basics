def calculator():

    math_operators_list = ['+', '-', '*', '/', '%']

    x = float(input("Enter your first number :"))
    y = float(input("Enter your second number :"))
    math_operator = input("Enter mathematical operators :")

    while math_operator not in math_operators_list:
        print("Invalid mathematical operator!")
        math_operator = input("Enter mathematical operators :")

    if math_operator == '+':
       result = x + y
    elif math_operator == '-':
       result = x - y
    elif math_operator == '*':
        result = x * y
    elif math_operator == '/':
        result = x / y
    else:
        result = x % y

    print(F"{x} {math_operator} {y} = {result}")


calculator()