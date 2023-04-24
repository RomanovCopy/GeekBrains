#Напишите программу вычислени арифметического выражения 
#заданного строкой.Используйте операции: + - / *
#Приоритет операций стандартный.



expression=input("Введите строку выражения : ")

expression_elements={}
element=[]
last=0
counter=0
for i in range(len(expression)):
    e=expression[i]
    if e=='+' or e=='-':
        element=[e,'o','sec',False]
    elif e=='/' or e=='*':
        element=[e,'o','first',False]
    elif e=='=':
        element=[e,'o','last',False]
    else:
        continue

    v=float(expression[last:i])
    expression_elements[counter]=[v,'num','' ,False]
    counter+=1
    expression_elements[counter]=element
    counter+=1
    last=i+1
    if last==len(expression):
        last=''
     

print(expression_elements)




