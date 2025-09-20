import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("Pasta1.xlsx", engine="openpyxl")

# Converter para datetime com timezone UTC
df['DataVersao'] = pd.to_datetime(df['DataVersao'], utc=True)

# Converter para horário de São Paulo
df['DataVersao'] = df['DataVersao'].dt.tz_convert('America/Sao_Paulo')

# Mostrar os Praetors disponíveis
praetors_disponiveis = df['Praetor'].unique()
print("Praetors disponíveis:", praetors_disponiveis)

# Solicitar ao usuário que escolha um Praetor
praetor_escolhido = int(input("Digite o número do Praetor que deseja analisar: "))

# Filtrar os dados pelo Praetor escolhido
filtro_df = df[df['Praetor'] == praetor_escolhido]

# Lista para armazenar os resultados
resultados = []

# Agrupar por ID
for id_valor, grupo in filtro_df.groupby('ID'):
    grupo = grupo.sort_values(by='DataVersao')  # garantir ordem cronológica
    tempos = {
        "ID": id_valor,
        "modo de falha": grupo['modo de falha'].iloc[0],
        "Praetor": grupo['Praetor'].iloc[0]
    }

    # Filtrar os status
    aberto = grupo[grupo['Status'].str.contains('Aberto', case=False)]['DataVersao']
    andamento = grupo[grupo['Status'].str.contains('Em andamento', case=False)]['DataVersao']
    encerrado = grupo[grupo['Status'].str.contains('Encerrado$', case=False)]['DataVersao']
    reaberto = grupo[grupo['Status'].str.contains('Reaberto', case=False)]['DataVersao']
    encerrado2 = grupo[grupo['Status'].str.contains('Encerrado 2', case=False)]['DataVersao']

    # Calcular os tempos em horas totais
    if not aberto.empty and not andamento.empty:
        delta = andamento.values[0] - aberto.values[0]
        horas_totais = round(delta / pd.Timedelta(hours=1), 2)
        tempos['Aberto -> Em andamento (horas)'] = horas_totais
        tempos['Hora Aberto'] = aberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Em andamento'] = andamento.dt.strftime('%H:%M:%S').values[0]

    if not andamento.empty and not encerrado.empty:
        delta = encerrado.values[0] - andamento.values[0]
        horas_totais = round(delta / pd.Timedelta(hours=1), 2)
        tempos['Em andamento -> Encerrado (horas)'] = horas_totais
        tempos['Hora Encerrado'] = encerrado.dt.strftime('%H:%M:%S').values[0]

    if not reaberto.empty and not encerrado2.empty:
        delta = encerrado2.values[0] - reaberto.values[0]
        horas_totais = round(delta / pd.Timedelta(hours=1), 2)
        tempos['Reaberto -> Encerrado 2 (horas)'] = horas_totais
        tempos['Hora Reaberto'] = reaberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Encerrado 2'] = encerrado2.dt.strftime('%H:%M:%S').values[0]

    resultados.append(tempos)

# Criar DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Mostrar no terminal
print(df_resultados)

# Salvar em Excel com nome personalizado
nome_arquivo = f"tempos_status_praetor_{praetor_escolhido}.xlsx"
df_resultados.to_excel(nome_arquivo, index=False)
print(f"Arquivo salvo como: {nome_arquivo}")
