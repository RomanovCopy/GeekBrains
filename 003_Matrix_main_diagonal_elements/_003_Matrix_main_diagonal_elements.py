# Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
#Выведите элементы главной диагонали матрицы в виде одномерного массива.


import numpy as np

#Случайные размеры массива
sizes = np.random.randint(5,10, size=2)

# Создание двумерного массива случайного размера
array = np.random.randint(1,100, size=(sizes[0],sizes[1]))

print(f"Создан массив с размерами {sizes[0]} на {sizes[1]} \n{array}")

# Нахождение индексов максимального и минимального элементов
max_index = np.unravel_index(np.argmax(array), array.shape)
min_index = np.unravel_index(np.argmin(array), array.shape)

print(f"Индексы максимального элемента: {max_index}")
print(f"Индексы минимального элемента: {min_index}")

# Вывод элементов главной диагонали
print(f"Главная диагональ массива:\n {np.diag(array)}" )
