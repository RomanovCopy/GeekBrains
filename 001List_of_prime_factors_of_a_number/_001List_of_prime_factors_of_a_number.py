
# Напишите метод, который вернёт список простых
# множителей числа N и количество этих множителей


# является ли число простым
def isPrime(n):
    # исключаем из проверки четные числа кроме двойки
    if n % 2 == 0:  
        return n == 2
    # исключаем четные и превосходящие квадраный корень из n делители
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

#простые множители
def primeFactors(n):
    d = []
    for i in range(2, n):
        if isPrime(i):
            while n%i==0:
                d.append(f'{i}, ')
                n/=i
    return d

prime_factors=primeFactors(int(input("Число : ")))

print(f"Найдено простых множителей: {len(prime_factors)} .\nСписок простых множителей : {''.join(prime_factors)}")