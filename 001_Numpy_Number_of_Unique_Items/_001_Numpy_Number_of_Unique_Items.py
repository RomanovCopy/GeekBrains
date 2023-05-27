#Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

my_list = [1, 2, 3, 4, 2, 3, 1, 5, 6, 7, 8, 6]

unique_elements, counts = np.unique(my_list, return_counts=True)

print("Уникальные элементы:", unique_elements)
print("Количество каждого элемента:", counts)
print("Количество уникальных элементов:", len(unique_elements))
