def sum(x):
    x+=5
    return x

a = lambda x: x+5
lst=[1,2,3,4,5]
print(list( map(a, lst)))
print(list(map(lambda x: x+5, lst)))
print(list(map(sum, lst)))
print(list(filter(lambda x: x>3, lst)))