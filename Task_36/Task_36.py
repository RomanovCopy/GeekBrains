#Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
#столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
#которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
#почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
#ровно два аргумента, как, например, у операции умножения.


from random import randint
#Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
#столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
#которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
#почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
#ровно два аргумента, как, например, у операции умножения.

def print_matrix(matrix):
    #печать нумерации столбцов
    print("   ", end="")
    for j in range(len(matrix[0])):
        print(j+1, end="\t")
    print()
    #печать строк с их нумерацией
    for i in range(len(matrix)):
        print(i+1, end=": ")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()


def print_operation_table(operation, num_rows=6, num_columns=6):
    #создание матрицы с заданными параметрами
    matrix = [[operation(i, j) for j in range(num_columns+1)[1:]] for i in range(num_rows+1)[1:]]
    #печать матрицы с нумерацией строк и столбцов
    print_matrix(matrix)

print_operation_table(lambda x,y:x*y)
