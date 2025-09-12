#Visualizar dados
import pandas as pd
import numpy as np


df = pd.read_excel("vendas_grande.xlsx")

print(df.head(3))
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.to_numpy())
print(df.T)