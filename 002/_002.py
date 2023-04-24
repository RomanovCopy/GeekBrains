#Даны два случайных пятизначных числа.
#Определить состоят ли они из одинаковых цифр.


a=int(input("number 1 :"))
b=int(input("number 2 :"))

d=True
for c in str(a):
    if c in str(b):
        d=False
        break
print(d)
