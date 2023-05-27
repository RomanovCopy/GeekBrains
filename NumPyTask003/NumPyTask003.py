#Задайте квадратную матрицу, состоящую из случайных чисел. Найдите самый часто встречающийся элемент в этой матрице.

import numpy as np

# Создание квадратной матрицы размера 5x5 из случайных чисел 
# от 0 до 9
matrix = np.random.randint(0, 9, size=(5, 5))
print(matrix)

# Подсчет количества вхождений каждого элемента в матрице
#flatten - перевод в одномерный список
counts = np.bincount(matrix.flatten())

# Находим индекс элемента с максимальным количеством вхождений
most_common_index = np.argmax(counts)

# Находим самый часто встречающийся элемент
most_common_element = most_common_index.item()

print("Самый часто встречающийся элемент:", most_common_element)