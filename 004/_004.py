#Имеется 1000 рублей. Бык стоит –100 рублей, корова –50 рублей, телёнок –5 рублей. 
#Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?

#summa=float(input("Общая сумма выделенная на закупки : "))
#heads=int(input("Общее колличество голов для закупки : "))
#bull=float(input("Стоимость быка : "))
#cow=float(input("Стоимость коровы : "))
#calf=float(input("Стоимость теленка : "))

summa=2000
heads=100
bull=100
cow=50
calf=5

for i in range(0,summa,bull):
    for j in range(0,summa,cow):
        for k in range(0,summa,calf):
            summ=i+j+k
            count=i/bull+j/cow+k/calf
            if summ==summa and count==heads:
                print(f"Быков: {i/bull}\nКоров: {j/cow}\nТелят: {k/calf}")
