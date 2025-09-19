import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("HistoricoVersoes (5).xlsx", engine="openpyxl")

# Converter a coluna de data para datetime
df['DataVersao'] = pd.to_datetime(df['DataVersao'])

# Lista para armazenar os resultados
resultados = []

# Agrupar por ID
for id_valor, grupo in df.groupby('ID'):
    grupo = grupo.sort_values(by='DataVersao')  # garantir ordem cronológica
    tempos = {
        "ID": id_valor,
        "modo de falha": grupo['modo de falha'].iloc[0],
        "Praetor": grupo['Praetor'].iloc[0],
        
    }

    # Filtrar os status
    aberto = grupo[grupo['Status'].str.contains('Aberto', case=False)]['DataVersao']
    andamento = grupo[grupo['Status'].str.contains('Em andamento', case=False)]['DataVersao']
    encerrado = grupo[grupo['Status'].str.contains('Encerrado$', case=False)]['DataVersao']
    reaberto = grupo[grupo['Status'].str.contains('Reaberto', case=False)]['DataVersao']
    encerrado2 = grupo[grupo['Status'].str.contains('Encerrado 2', case=False)]['DataVersao']

    # Calcular os tempos
    if not aberto.empty and not andamento.empty:
        tempos['Aberto -> Em andamento'] = andamento.values[0] - aberto.values[0]
        tempos['Hora Aberto'] = aberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Em andamento'] = andamento.dt.strftime('%H:%M:%S').values[0]

    if not andamento.empty and not encerrado.empty:
        tempos['Em andamento -> Encerrado'] = encerrado.values[0] - andamento.values[0]
        tempos['Hora Encerrado'] = encerrado.dt.strftime('%H:%M:%S').values[0]

    if not reaberto.empty and not encerrado2.empty:
        tempos['Reaberto -> Encerrado 2'] = encerrado2.values[0] - reaberto.values[0]
        tempos['Hora Reaberto'] = reaberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Encerrado 2'] = encerrado2.dt.strftime('%H:%M:%S').values[0]

    resultados.append(tempos)

# Criar DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Mostrar no terminal
print(df_resultados)

# Salvar em Excel
df_resultados.to_excel("tempos_status_com_falha.xlsx", index=False)
