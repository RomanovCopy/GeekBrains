#Создайте декоратор повторяющий функцию 
#заданное количество раз.

def decorator(func):
    count=5
    def dec(count):
        for i in range(count):
            func()


@decorator
def my_print():
    print("Romanov")