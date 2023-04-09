#Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
def factorial(number):
    f=1
    for c in range(1, number+1):
        f*=c
    return f

N=int(input("Введите конечное значение последовательности : "))
#два цикла только для печати

#вывод списка чисел
for r in range(1,N+1):
    print(r, end='\t')
print()

#вывод факториалов для каждого элемента списка
for n in range(1, N+1):
    print(factorial(n), end='\t')

