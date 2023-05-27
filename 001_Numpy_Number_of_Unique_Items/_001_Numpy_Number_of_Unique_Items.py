#Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

my_list = np.random.randint(1, 10, size=20)

print(f"Создан список : {my_list}")
print(f"Количество уникальных элементов : {len( np.unique(my_list))}", )
