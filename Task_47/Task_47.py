
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
from random import randint


values = list(randint(0, 100) for _ in range(10))
print(values)
transformed_values = list(map(lambda x: x, values))
print(transformed_values)
