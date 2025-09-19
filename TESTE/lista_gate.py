# import pandas as pd

# df = pd.read_csv("Lista.csv")
# df.head()
# df.tail()
# print(df)
# colunas= pd.set_option('Display.max_columns', None)
# print(colunas)


import pandas as pd

# Configura o Pandas para mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Lê o arquivo CSV
df = pd.read_csv('Lista.csv')

# Exibe o DataFrame
print(df)
