#Создайте декоратор повторяющий функцию 
#заданное количество раз.

def repeat(n):
    def our_repeat(func):
        def decorator(*args):
            for i in range(n):
                func(args[0])
        return decorator
    return our_repeat


@repeat(3)
def my_print(text):
    print(text)


my_print("Hello World!")
