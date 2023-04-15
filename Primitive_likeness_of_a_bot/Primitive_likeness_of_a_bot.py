myDict={}
def closing():
     with open("myDict.txt", "w", encoding="utf-8") as file:
         for key in myDict:
             myDict[key]=myDict[key].replace('\n', '')
             file.write(f"{key}:{str(myDict[key])}\n")

def loaded():
    myDict.clear()
    with open("myDict.txt", "r", encoding="utf-8") as file:
         for line in file.readlines():
             array=line.split(':')
             myDict[array[0]]=''.join(array[1:]).replace('\n','')
            

loaded()

print("Задайте вопрос... Для окончания диалога введите пустую строку")
answer="?"
while len(answer)>0:
    k=input()
    if k in myDict:
        print(myDict[k])
    else:
        print("А что вы скажете в такой ситуации? ")
        answer=input()
        if len(answer)>0:
            myDict[k]=answer

closing()
print(myDict)
 
