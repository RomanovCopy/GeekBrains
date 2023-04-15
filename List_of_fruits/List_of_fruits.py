#В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву
print("Введите названия фруктов через пробел :")
array=input().split(' ')
length=len(array)
lst=[array[i] for i in range(length)]
key=input("Первые буквы фрукта : ").lower()
for n in lst:
    if n[:len(key)].lower()==key:
        print(n, end=',')


