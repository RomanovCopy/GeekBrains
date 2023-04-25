#Калькулятор для вычисления строковых выражений


numbers=['1','2','3','4','5','6','7','8','9','0']
expression_elements=[]

#парсинг строки
def expression_parsing(expression):
    for i in range(len(expression)):
        e = expression[i]
        if e == '+' or e == '-' or e == '/' or e == '*':
            i+=1
            while i<len(expression) and (expression[i] in numbers or expression[i]==' '):
                if expression[i] in numbers:
                    e=f"{e}{expression[i]}"
                i+=1
            expression_elements.append(e)
        elif e == '=':
            break
        else:
            continue


#исполнитель
def execute(index):
    result=0
    e=expression_elements[index]
    if index>0:
        if str(e).__contains__('+') or str(e).__contains__('-'):
            result=float(e)+float(expression_elements[index-1])
            expression_elements[index-1]=0
        elif str(e).__contains__('*'):
            result=float(str(e).replace('*',''))*float(expression_elements[index-1])
            expression_elements[index-1]=0
        elif str(e).__contains__('/'):
            result=float(expression_elements[index-1])/float(str(e).replace('/',''))
            expression_elements[index-1]=0
    else:
        result=float(e)
    return result


def processing():
    result=0
    for index in range(len(expression_elements)):
        e=str(expression_elements[index])
        if  e.__contains__('*') or e.__contains__('/'):
            expression_elements[index]=execute(index)
    for index in range(len(expression_elements)):
        e=str(expression_elements[index])
        if  e.__contains__('+') or e.__contains__('-'):
            expression_elements[index]=execute(index)
    for index in range(len(expression_elements)):
        result+=expression_elements[index]
    print(result)


def expression_input():
    c=''
    c = input("Введите выражение. В конце обязателен '=' : ")
    if len(c)>3:
        if c[0]!='-' and c[0]!='+':
            c=f"+{c}"
    expression_parsing(c)
    processing()
    


expression_input()
