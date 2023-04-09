str1=input("Подстрока : ")
str2=input("Строка : ")
len1=len(str1)
len2=len(str2)
count = 0
for i in range(len2-len1+1):
        if str1 == str2[i:i+len1]:               count += 1
print(count)
            
