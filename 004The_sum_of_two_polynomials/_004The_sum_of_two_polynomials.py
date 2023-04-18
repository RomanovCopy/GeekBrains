

#считывание строки из файла
def reading_data(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readline()

#разбиение многочлена на одночлены
def division_into_monomials2(polynomial):
    p = str(polynomial).replace("\n", "")
    length = len(p)
    count = 0
    i = 0
    coeff = {}
    var = {}
    deg = {}
    while i < (len(p)):
        if p[i].isdigit() or p[i] == "^":
            if p[i] == "^":
                k = str("^")
                i += 1
            else:
                k = str("")
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


def addition_of_monomials(mono1, mono2):
    m1=str('')
    m2=str('')
    for ch in str(mono1):
        if ch.isalpha() or ch=='^':
            m1+=ch
    if len(m1)>0:
        m2 = str(mono2).__contains__(m1)
    return m2



polynomial1 = reading_data("polynomial1.txt")
polynomial2 = reading_data("polynomial2.txt")
polynom1 = division_into_monomials2(polynomial1)
polynom2 = division_into_monomials2(polynomial2)
addition_of_monomials('25x^2', '2.3x^2 + x + 8' )
print(f"{polynom1}\n{polynom2}")
