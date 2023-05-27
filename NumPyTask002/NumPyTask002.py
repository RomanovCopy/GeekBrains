import numpy as np


size=10
#массив случайных чисел от 0 до 5 из 10 элементов
numbers=np.random.randint(10,100,size)
print(numbers)

#среднее арифметическое списка
mean=np.mean(numbers)
print(mean)

#ближайшие по значению к числу 20 и его индекс

dist=[np.abs(el-20) for el in numbers]
print(dist)#список разниц
minDist=np.min(dist)
print(f"Минимальное расстояние: { minDist }")
print(f"Индекс : {dist.index(minDist)}")