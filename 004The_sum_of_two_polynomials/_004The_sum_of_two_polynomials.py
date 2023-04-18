

##считывание строки из файла
#def reading_data(path):
#    with open(path, "r", encoding="utf-8") as file:
#        return file.readline().replace('\n','')

#разбиение многочлена на одночлены
#def division_into_monomials2(polynomial):
#    p = str(polynomial).replace("\n", "")
#    length = len(p)
#    count = 0
#    i = 0
#    coeff = {}
#    var = {}
#    deg = {}
#    while i < (len(p)):
#        if p[i].isdigit() or p[i] == "^":
#            if p[i] == "^":
#                k = str("^")
#                i += 1
#            else:
#                k = str("")
#            j = i
#            while j < length and (p[j].isdigit() or p[j] == "."):
#                k += str(p[j])
#                j += 1
#            i = j
#            if k.__contains__("^"):
#                deg[count] = k
#            else:
#                coeff[count] = k
#            count += 1
#        elif p[i].isalpha():
#            j = i
#            k = str("")
#            while j < length and p[j].isalpha():
#                k += str(p[j])
#                j += 1
#            i = j
#            var[count] = k
#            count += 1
#        elif p[i] == "-" or p[i] == "+":
#            var[count] = p[i]
#            count += 1
#            i += 1
#        else:
#            i += 1
#    return coeff, var, deg


#def addition(poly1,poly2):
#    length1=0
#    for d in poly1:
#        length1+=len(d)
#    for i in range(length1):
#        if i in poly1[0]:
#            a=i


    



#polynomial1 = reading_data("polynomial1.txt")
#polynomial2 = reading_data("polynomial2.txt")
#polynom1 = division_into_monomials2(polynomial1)
#polynom2 = division_into_monomials2(polynomial2)
#print(f"{polynom1}\n{polynom2}")


# coeffs - список коэффициентов многочлена
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs=coeffs
        #сложение двух многочленов 
        #с созданием третьего
    def __add__(self, other):
        if len(self.coeffs)>len(other.coeffs):
            coeffs=self.coeffs[:]
            for i in range(len(other.coeffs)):
                coeffs[i]+=other.coeffs[i]
        else:
            coeffs=other.coeffs[:]
            for i in range(len(self.coeffs)):
                coeffs[i]+=self.coeffs[i]
        return Polynomial(coeffs)
    #преобразование многочлена в строку для вывода
    def __str__(self):
        terms=[]
        for i, coeff in enumerate(self.coeffs):
            if coeff==0:
                continue
            elif i==0:
                terms.append(str(coeff))
            elif i==1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{i}")
        return " + ".join(terms)

p1=Polynomial([5, 3])#5x^2 + 3x создание первого многочлена
p2=Polynomial([3, 1, 8])#2. 3x^2 + x + 8 создание второго многочлена
p3=p1+p2#сложение двух многочленов
print(p3)#8x^2 + 4x + 8