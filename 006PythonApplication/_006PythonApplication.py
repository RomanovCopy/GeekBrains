number=int(input("Число? :"))
r=range(1,number+1)
for i in r:
    if number%i==0:
        if i%2==0:
            print(i)

