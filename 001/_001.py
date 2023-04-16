#Создайте кортеж. Запишите в него 10 случайных чисел
import random
a=tuple(random.randint(1,10) for _ in range(10))
print(a)
