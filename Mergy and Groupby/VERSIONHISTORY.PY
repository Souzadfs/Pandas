import pandas as pd

df = pd.read_excel("HistoricoVersoes (6).xlsx", engine="openpyxl")


df['DataVersao'] = pd.to_datetime(df['DataVersao'])

df['DataFormatada'] = df['DataVersao'].dt.strftime('%d/%m/%Y %H:%M:%S')



#df.head()

print(df)