#Напишите функцию same_by(characteristic, objects), которая 
#проверяет, все ли объекты имеют одинаковое значение 
#некоторой характеристики, и возвращают True, если это так. 
#Если значение характеристики для разных объектов 
#отличается - то False. Для пустого набора объектов, функция 
#должна возвращать True. Аргумент characteristic - это 
#функция, которая принимает объект и вычисляет его 
#характеристику.


def same_by(characteristic, objects):
    list_values=[characteristic(obj) for obj in objects ]#список результатов
    return all(value for value in list_values)#все результаты в списке = True


values = [0, 2, 10, 6]#список значений для проверки
characteristic=lambda x:x%2==0 #условие проверки(кратность двум)


if same_by(characteristic, values):
    print('same')
else:
    print('different')


     