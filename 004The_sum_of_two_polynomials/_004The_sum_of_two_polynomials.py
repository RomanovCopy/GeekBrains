

#считывание строки из файла
def reading_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readline().replace('\n','')

#разбиение многочлена на одночлены
#на вход подается многочлен в виде строки
def division_into_monomials2(polynomial):
    p = str(polynomial)
    length = len(p)
    count = 0
    i = 0
    coeff = {}#словарь коэффициентов(позиция в многочлене : значение)
    var = {}#словарь переменных(позиция в многочлене : значение)
    deg = {}#словарь степеней(позиция в многочлене : значение)
    num=False
    while i < (len(p)):
        if p[i].isdigit() or p[i] == "^":
            if p[i] == "^":
                k = str("^")
                i += 1
            else:
                k = str("")
                num=True
            j = i
            while j < length and (p[j].isdigit() or p[j] == "."):
                k += str(p[j])
                j += 1
            i = j
            if k.__contains__("^"):
                deg[count] = k
            else:
                coeff[count] = k
            count += 1
        elif p[i].isalpha():
            j = i
            k = str("")
            if num==False:
                coeff[count]=1
            else:
                num=False
            while j < length and p[j].isalpha():
                k += str(p[j])
                j += 1
            i = j
            var[count] = k
            count += 1
        elif p[i] == "-" or p[i] == "+":
            var[count] = p[i]
            count += 1
            i += 1
        else:
            i += 1
    return coeff, var, deg


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
    

polynomial1 = reading_data("polynomial1.txt")
polynomial2 = reading_data("polynomial2.txt")
polynom1 = division_into_monomials2(polynomial1)
polynom2 = division_into_monomials2(polynomial2)
koeff1=[]
koeff2=[]
for i in polynom1[0]:
    koeff1.append(float(polynom1[0][i]))
for i in polynom2[0]:
    koeff2.append(float(polynom2[0][i]))


p1=Polynomial(koeff1)#5x^2 + 3x создание первого многочлена
p2=Polynomial(koeff2)#2. 3x^2 + x + 8 создание второго многочлена
p3=p1+p2#сложение двух многочленов
print(p3)#8x^2 + 4x + 8