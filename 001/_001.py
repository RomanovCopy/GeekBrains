import random
numbers=[0]
length=10
numbers=numbers*length
#������� ������
for index in range(len(numbers)):
    numbers[index]=random.randint(0,10)
print(numbers)

#� ������� ����������
numbers=[random.randint(0,10) for el in range(length)]
print(numbers)

