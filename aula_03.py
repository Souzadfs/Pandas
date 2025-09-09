import pandas as pd
import numpy as np

datas = pd.date_range('20250908', periods= 60, freq= "D")
df = pd.DataFrame(np.random.randn(60,5), index= datas, columns= list("ABCDE"))



print(df.head(3))

df['F'] = 1
df['G'] = range(60)
df['Produto'] = df['A'] * df['B']
df['Maximo'] = df['A'].max()
df['Minimo'] = df['A'].min()
df['Média'] = df['A'].mean()
print(df, df.shape)