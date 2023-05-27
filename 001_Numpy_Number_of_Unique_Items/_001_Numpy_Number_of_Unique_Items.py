#Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

my_list = np.random.randint(1, 100, size=20)

#unique_elements, counts = np.unique(my_list, return_counts=True)

print(f"Создан список : {my_list}")
print(f"Количество уникальных элементов : {len( np.unique(my_list))}", )
#print("Количество каждого элемента:", counts)
#print("Количество уникальных элементов:", len(unique_elements))
