
# Даны два файла, в каждом из которых находится запись многочлена.
# Найдите сумму данных многочленов




def reading_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()

#разбиение многочлена на одночлены
def division_into_monomials(polynomial):
    set1={'+', '-'}
    set2={'*', '/', '.','^'}
    p = str(polynomial).replace('\n', '')
    length = len(p)
    count = 0
    mono = []
    poly=[]
    while count<length:
        if p[count].isdigit() or p[count].isalpha() or len( set( p[count]).intersection(set2))>0:
            mono.append( p[count])
            if count==length-1:
                poly.append(mono)
        elif len( set( p[count]).intersection(set1))>0 or count==length-1:
                poly.append(mono.copy())
                poly.append(p[count])
                mono.clear()
        count+=1
    return poly

#приведение подобных членов
#def ghost_like_members(polynomial):
#    last=""
#    for mono in polynomial:
#        for i in range(len(mono)):
#            if mono[i].isdigit and last=='digital':





polynomials = reading_data("polynomials.txt")
polynom1 = division_into_monomials( polynomials[0])
polynom2 = division_into_monomials(polynomials[1])
print(f"{polynom1}\n{polynom2}")
