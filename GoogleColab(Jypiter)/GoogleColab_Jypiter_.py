import pandas as pd

df=pd.read_csv("california_housing_test.csv")
#print(df.head(n=20))#вывод первых n строк таблицы
print(df.tail(n=20))#вывод последних n строк таблицы
