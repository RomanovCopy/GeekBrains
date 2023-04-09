#Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z
print("Таблица истинности для выражения ¬(X ∧ Y) ∨ Z")
print("X\tY\tZ\tResult")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"{x}\t{y}\t{z}\t{bool(not(x or y)and z )}")

