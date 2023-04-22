#На вход подаётся четырёхзначное число. 
#Получите список, состоящий из цифр данного числа, 
#увеличенных на 10.

from random import randint
num = str(randint(1000, 10000))
lst = [i for i in num]
print(lst)
lst_num = list(map(lambda x: int(x) * 10, lst))
print(lst_num)