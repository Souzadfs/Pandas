import pandas as pd

# Mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Carregar o arquivo Excel
df = pd.read_excel("HistoricoVersoes1.xlsx", engine="openpyxl")

# Exibir o DataFrame
print(df)
