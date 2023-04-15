import random

length=30
sum1=0
sum2=0
l=[random.randint(0,25) for i in range(length+1)]
for j in range(length):
    if j<=int(length/2):
        sum1+=l[j]
    else:
        sum2+=l[j]
print(sum1>=sum2)

