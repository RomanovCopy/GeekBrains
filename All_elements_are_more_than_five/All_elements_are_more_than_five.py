#Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
#Используйте для решения лямбда-функцию


from random import randint

s = int(input("Размер списка : "))
v2=lambda: [randint(1, 11) for _ in range(s)]
lst=[filter(v2 )]
print(  )
