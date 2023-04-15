import random
numbers=[0]
length=10
numbers=numbers*length
#обычный способ
for index in range(len(numbers)):
    numbers[index]=random.randint(0,10)
print(numbers)

#с помощью генератора
numbers=[random.randint(0,10) for el in range(length)]
print(numbers)

