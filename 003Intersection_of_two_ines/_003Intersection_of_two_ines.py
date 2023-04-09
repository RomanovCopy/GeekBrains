#Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй


#удаление повторов
def res(listing):
    length=len(listing)
    for i in range(length):
        for j in range( i+1, length):
            if j<length and listing[i]==listing[j]:
                listing.pop(j)
    return listing


substring=input("Подстрока : ")
string=input("Строка : ")
temp=[]
#первичный подсчет
for ss in substring:
    c=0
    for s in string:
        if ss==s:
            c+=1
    temp.append((ss,c))
print(res(temp))#выводим результат без повторов



