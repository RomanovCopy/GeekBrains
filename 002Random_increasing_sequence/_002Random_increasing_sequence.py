
# Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие случайную возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import randint


def sequence(lst):
    last = lst[0]
    for i in range(0, len(lst)):
        if lst[i] >= last:
            last = lst[i]
            if lst[i] not in lst1:  # исключение повторений
                lst1.append(lst[i])
    return lst1


n = int(input("Размер исходного списка : "))
lst = [randint(0, 100) for _ in range(n)]  # генератор списка
lst1 = []
print(f"Исходный список :\n {lst}")
print("Все возможные возрастающие последовательности из исходного списка :")
while len(lst) > 1:
    lst1.clear()
    lst1 = sequence(lst)
    lst = lst[1:]#срез для обновления первого значения последовательности
    if len(lst1) > 1:#последовательности длиной менее двух чисел нас не интересуют
        print(lst1)