#Дан список случайных элементов. Необходимо убедиться, что 
#все элементы являются уникальными

from random import randint

lst=[randint(0, 100) for _ in range(20)]

print(lst, len(set(lst))==len(lst))