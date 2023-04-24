
# Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет, есть в массиве
# последовательность из трёх элементов, совпадающая с введённым числом.

from random import randint

arr = []


def generator():
    return [randint(0,9) for _ in range(15)]


def sequence_search(number):
    string=''
    for c in arr:
        string+=str(c)
    if string.__contains__(number):
        print(number)


arr = generator()
print(arr)
sequence_search(input("Трехзначное число : "))