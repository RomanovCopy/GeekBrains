
# Напишите метод, который вернёт список простых
# множителей числа N и количество этих множителей


# является ли число простым
def isPrime(n):
    if n % 2 == 0:  # исключаем из проверки четные числа
        return n == 2
    # исключаем четные и превосходящие квадраный корень из n делители
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def primeFactors(n):
    d = []
    for i in range(2, n):
        if isPrime(i) and n % i == 0:
            d.append(f'{i}, ')
    return d

prime_factors=primeFactors(int(input("Число : ")))

print(f"Найдено {len(prime_factors)} простых множителей.\nПростые множители : {''.join(prime_factors)}")