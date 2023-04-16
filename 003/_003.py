
# На вход подаются два числа. Напишите метод, который вернёт
# сумму, разность, произведение и частное этих чисел.
def res(a, b):
    return a + b, a * b, a - b, a / b


s, p, r, ch = res(int(input("A")), int(input("B")))

print(s, p, r, ch)
