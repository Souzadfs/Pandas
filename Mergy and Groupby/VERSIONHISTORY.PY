import pandas as pd

df = pd.read_excel("HistoricoVersoes (6).xlsx", engine="openpyxl")


df['DataVersao'] = pd.to_datetime(df['DataVersao'])

df['DataFormatada'] = df['DataVersao'].dt.strftime('%H:%M:%S')

resultados = []

for id_valor, grupo in df.groupby('ID'):
    tempos = {"ID": id_valor}
    
    aberto = grupo[grupo['Status'].str.contains('Aberto|Reaberto', case=False)]['DataVersao']
    andamento = grupo[grupo['Status'].str.contains('Executado|Em andamento', case=False)]['DataVersao']
    encerrado = grupo[grupo['Status'].str.contains('Encerrado', case=False)]['DataVersao']

    if not aberto.empty and not andamento.empty:
        tempos['Aberto/Reaberto -> Em andamento'] = andamento.values[0] - aberto.values[0]
        tempos['Hora Aberto/Reaberto'] = aberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Em andamento'] = andamento.dt.strftime('%H:%M:%S').values[0]
    if not andamento.empty and not encerrado.empty:
        tempos['Em andamento -> Encerrado'] = encerrado.values[0] - andamento.values[0]
        tempos['Hora Encerrado'] = encerrado.dt.strftime('%H:%M:%S').values[0]

    resultados.append(tempos)



#df.head()

print(pd.DataFrame(resultados))
