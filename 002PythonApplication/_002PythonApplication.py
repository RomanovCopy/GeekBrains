
number=1
count=0
while number!=0:
    number= float(input('Number? '))
    print()
    if number%3==0 and number!=0:
        count+=1
print(f'End {count}')

