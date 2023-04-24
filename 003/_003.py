
# Напишите программу вычислени арифметического выражения
# заданного строкой.Используйте операции: + - / *
# Приоритет операций стандартный.


def expression_parsing(expression):
    expression_elements = {}
    element = []
    last = 0
    counter = 0
    for i in range(len(expression)):
        e = expression[i]
        if e == "+" or e == "-":
            element = [e, "o", "sec", False]
        elif e == "/" or e == "*":
            element = [e, "o", "first", False]
        elif e == "=":
            element = [e, "o", "last", False]
        else:
            continue
        v = float(expression[last:i])
        expression_elements[counter] = [v, "num", "", False]
        counter += 1
        expression_elements[counter] = element
        counter += 1
        last = i + 1
    return expression_elements

def calculation(expression_elements):
    e=expression_elements
    for key in e :
        if e[key][1]=='o':



expression = expression_parsing(input("Введите строку выражения : "))
calculation(expression)

