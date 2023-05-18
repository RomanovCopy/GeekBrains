#Напишите функцию find_farthest_orbit(list_of_orbits), 
#которая среди списка орбит планет найдет ту, 
#по которой вращается самая далекая планета. Результатом 
#функции должен быть кортеж, содержащий длины полуосей 
#эллипса орбиты самой далекой планеты. Каждая орбита 
#представляет из себя кортеж из пары чисел - полуосей ее 
#эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
#где a и b - длины полуосей эллипса. При решении задачи 
#используйте списочные выражения. Подсказка: проще всего 
#будет найти эллипс в два шага: сначала вычислить самую 
#большую площадь эллипса, а затем найти и сам эллипс, 
#имеющий такую площадь. Гарантируется, что самая далекая 
#планета ровно одна

from math import pi
from random import randint

list_of_orbits= list((randint(10,20), randint(10,20)) for _ in range(5))

def find_farthest_orbit(list_of_orbits):
     orbit_area=list(map(lambda x: pi*x[0]*x[1], list_of_orbits))
     print(f"Площади орбит : {orbit_area}")
     return list_of_orbits[orbit_area.index(max(orbit_area))]

print(f"Орбиты планет : {list_of_orbits}" )
print( f"Орбита самой далекой планеты : {find_farthest_orbit(list_of_orbits)}")