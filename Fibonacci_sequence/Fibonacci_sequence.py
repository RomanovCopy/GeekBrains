 #Создайте список. Запишите в него N первых элементов последовательности Фибоначчи
def fibonacci(number):
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

n=abs(int(input('Количество чисел последовательности : ')))
lst=[fibonacci(i) for i in range(1, n)]
print(lst)
