import pandas as pd

df = pd.read_csv("Lista.csv")
df.head()
df.tail()
print(df)
df.set_option('Lista.csv', None)
print(df)