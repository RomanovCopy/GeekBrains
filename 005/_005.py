dict = {'Ручка':5, 'карандаш':3, 'ластик':4}
sum = 0
flag = True
while flag:
    code = input('Введите наименование: ')
    if code in dict:
        sum += dict[code]
    elif code == 'стоп':
        flag = False          
print(sum)
