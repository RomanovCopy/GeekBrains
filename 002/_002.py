#замена элемента в кортеже
import random
n=int(input("Длина кортежа : "))
t=tuple(random.randint(0,100) for _ in range(n))
print(t)
n1=int(input("Индекс для замены :"))
v=input("Значение : ")
t=t[:n1] + (v,) + t[n1+1:]
print( t )