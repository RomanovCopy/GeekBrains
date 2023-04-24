#Найдите все простые несократимые дроби, лежащие между 0 и 1, 
#знаменатель которых не превышает 11.

#есть ли общий делитель
def is_common_divisor(numerator, denominator):
    for i in range(2,12):
        if numerator%i==0 and denominator%i==0:
            return True
    return False

for i in range(1,12):
    for j in range(i+1,12):
        if not is_common_divisor(i, j):
            print(f"{i}/{j}")