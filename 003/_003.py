
# Напишите программу вычислени арифметического выражения
# заданного строкой.Используйте операции: + - / *
# Приоритет операций стандартный.

#Примерный алгоритм
#1. Разбить строку на операнды и операторы.
#2. Определить приоритет операторов.
#3. Выполнить операции с наивысшим приоритетом.
#4. Заменить результат операции в выражении.
#5. Повторять шаги 3-4 до тех пор, пока не останется один операнд.
#6. Вернуть результат.

numbers=[1,2,3,4,5,6,7,8,9,0]
expression_elements=[]

#парсинг строки
def expression_parsing(expression):
    for i in range(len(expression)):
        e = expression[i]
        if e == '+' or e == '-' or e == '/' or e == '*':
            expression_elements.append(e)
        elif e == '=':
            break
        elif e in numbers:
            print()
        else:
            continue

#сложение
def summation(expression_elements, key):
    key1=expression_elements[key-1]
    key2=expression_elements[key+1]
    return key1[0]+key2[0]
#вычитание
def subtraction(expression_elements, key):
    key1=expression_elements[key-1]
    key2=expression_elements[key+1]
    return key1[0]-key2[0]
#умножение
def multiplication(expression_elements, key):
    key1=expression_elements[key-1]
    key2=expression_elements[key+1]
    return key1[0]*key2[0]
#деление
def division(expression_elements, key):
    key1=expression_elements[key-1]
    key2=expression_elements[key+1]
    return key1[0]/key2[0]
#исполнитель
def execute(expression_elements, key):
    e=expression_elements
    if e[key][0]=='+':
        return summation(e,key)
    elif e[key][0]=='-':
        return subtraction(e, key)
    elif e[key][0]=='*':
        return multiplication(e,key)
    elif e[key][0]=='/':
        return division(e,key)
#вычисления завершены?
def ready(expression_elements, key, result):
    e=expression_elements
    key1=key-1
    key2=key+1
    del(e[key2])
    if key1>=0:
       del(e[key1])
    e[key][0]=result
    e[key][1]='num'
    e[key][3]=True
    return e

#расчет
def calculation(expression_elements):
    e=expression_elements
    result=0
    for key in e :
        if e[key][2]=='first':
            result=execute(e,key)
    print(ready(e,1,result))
            

def expression_input():
    c=''
    c = input("Введите выражение : ")
    if len(c)>3:
        if c[0]!='-':
            c=f"+{c}"
    print(int(c))
    #expression_parsing(c)


expression_input()




