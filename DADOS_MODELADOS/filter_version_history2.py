import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("HistoricoVersoes.xlsx", engine="openpyxl")

# Converter para datetime com timezone UTC
df['DataVersao'] = pd.to_datetime(df['DataVersao'])

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
    grupo = grupo.sort_values(by='DataVersao') 
    tempos = {
        "ID": id_valor,
        "Modo de Falha": grupo['Modo de Falha'].iloc[0],
        "Descrição do Defeito":grupo['Descrição do Defeito'].iloc[0],
        "Praetor": grupo['Praetor'].iloc[0],
        "inpeção": grupo['inpeção'].iloc[0],
        "Região": grupo['Região'].iloc[0],
        "resp. Produção": grupo['resp. Produção'].iloc[0]
    }

    # Filtrar os status
    aberto = grupo[grupo['Status'].str.contains('Aberto', case=False)]['DataVersao']
    andamento = grupo[grupo['Status'].str.contains('Em andamento', case=False)]['DataVersao']
    Executado = grupo[grupo['Status'].str.contains('Executado$', case=False)]['DataVersao']
    reaberto = grupo[grupo['Status'].str.contains('Reaberto', case=False)]['DataVersao']
    executado2 = grupo[grupo['Status'].str.contains('Executado 2', case=False)]['DataVersao']
    encerrado_qualidade = grupo[grupo['Status'].str.contains('Encerrado Somente Qualidade e Delegado', case=False)]['DataVersao']

    # Calcular os tempos
    if not aberto.empty and not andamento.empty:
        tempos['Aberto -> Em andamento'] = andamento.values[0] - aberto.values[0]
        tempos['Hora Aberto'] = aberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Em andamento'] = andamento.dt.strftime('%H:%M:%S').values[0]

    if not andamento.empty and not Executado.empty:
        tempos['Em andamento -> Executado'] = Executado.values[0] - andamento.values[0]
        tempos['Hora Executado'] = Executado.dt.strftime('%H:%M:%S').values[0]

    if not reaberto.empty and not executado2.empty:
        tempos['Reaberto -> Executado 2'] = executado2.values[0] - reaberto.values[0]
        tempos['Hora Reaberto'] = reaberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Executado 2'] = executado2.dt.strftime('%H:%M:%S').values[0]

    if not Executado.empty and not encerrado_qualidade.empty:
        tempos['Executado -> Encerrado Qualidade'] = encerrado_qualidade.values[0] - Executado.values[0]
        tempos['Hora Executado'] = encerrado_qualidade.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Encerrado Qualidade'] = Executado.dt.strftime('%H:%M:%S').values[0] 
    
    if not reaberto.empty and not executado2.empty:
        tempos['Executado 2 -> Encerrado Qualidade'] = encerrado_qualidade.values[0] - executado2.values[0]
        tempos['Hora Reaberto'] = reaberto.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Encerrado Qualidade'] = executado2.dt.strftime('%H:%M:%S').values[0] 
    
    if not aberto.empty and not encerrado_qualidade.empty:
        tempos['aberto -> Encerrado Qualidade'] = encerrado_qualidade.values[0] - aberto.values[0]
        tempos['Hora aberto'] = encerrado_qualidade.dt.strftime('%H:%M:%S').values[0]
        tempos['Hora Encerrado Qualidade'] = aberto.dt.strftime('%H:%M:%S').values[0] 

    resultados.append(tempos)

# Criar DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Mostrar no terminal
print(df_resultados)

# Salvar em Excel com nome personalizado
nome_arquivo = f"tempos_status_praetor_{praetor_escolhido}.xlsx"
df_resultados.to_excel(nome_arquivo, index=False)
print(f"Arquivo salvo como: {nome_arquivo}")
