#Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

import numpy as np

# Создание двумерного массива размером 5х5
matrix = np.random.randint(1, 10, size=(5, 5))

print("Создана матрица:\n", matrix)

#список из одинковых строк
unique_rows = np.unique(matrix, axis=0)
#уникальных строк
unique_rows_len=unique_rows.shape[0]
#строк в начальной матрице
matrix_len=matrix.shape[0]
#если unique_rows_len и matrix_len равны то одинаковых строк нет
if unique_rows_len == matrix_len:
    print("Одинаковых строк нет")
else:
    print("Найдены одинаковые строки")