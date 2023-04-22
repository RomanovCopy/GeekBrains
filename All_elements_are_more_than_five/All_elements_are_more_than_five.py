#Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
#Используйте для решения лямбда-функцию


from random import randint

s = int(input("Размер списка : "))
lst = [randint(1, 11) for _ in range(s)]
print(f"Сгенерированный список : {lst}")
print(f"Элементы списка большие чем 5 : {list(filter(lambda x: x>5,lst))}")
