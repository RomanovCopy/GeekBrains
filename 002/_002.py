#С помощью анонимной функции найдите в списке на 15 элементов 
#числа, кратные 5. Заполните список случайным образом 
#числами от 1 до 100.
from random import randint
lst = [randint(1, 101) for i in range(15)]
print(lst)
lst_new = list(filter(lambda x: x % 5 == 0, lst))
print(lst_new)