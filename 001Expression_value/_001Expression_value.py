#Дано натуральное число N. 
#Найдите значение выражения:N + NN + NNN
#N может быть любой длины.

n=input("Целое положительное число : ")
lst=[ n for _ in range(3) ]#создаем список строк
lst1=[ int(''.join( lst[i:])) for i in range(3) ]  #объединяем строки и преобразуем в int
lst1.reverse()
#summ=sum(lst1)
print( f"{''.join(str(lst1))} => {sum(lst1)}")

#for i in range(2, -1, -1):#суммирование и вывод
#    summ+=lst1[i]
#    print(f"{lst1[i]} => {summ}" )
