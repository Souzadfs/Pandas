import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("HistoricoVersoes1.xlsx", engine="openpyxl")

# Converter para datetime
df['DataVersao'] = pd.to_datetime(df['DataVersao'])

# Ajustar timezone
if df['DataVersao'].dt.tz is None:
    df['DataVersao'] = df['DataVersao'].dt.tz_localize('UTC')
df['DataVersao'] = df['DataVersao'].dt.tz_convert('America/Sao_Paulo')

# Mostrar os Praetors disponíveis
praetors_disponiveis = df['Praetor'].unique()
print("Praetors disponíveis:", praetors_disponiveis)

# Escolher Praetor
praetor_escolhido = int(input("Digite o número do Praetor que deseja analisar: "))
filtro_df = df[df['Praetor'] == praetor_escolhido]

# Lista de resultados
resultados = []

# Função para converter timedelta em fração de dia com base nas horas totais
def horas_em_fracao_dia(td):
    td = pd.Timedelta(td)
    horas = td.total_seconds() / 3600
    return round(horas / 24, 15)  # fração de 1 dia

# Agrupar por ID
for id_valor, grupo in filtro_df.groupby('ID'):
    grupo = grupo.sort_values(by='DataVersao')
    tempos = {
        "ID": id_valor,
        "Modo de Falha": grupo['Modo de Falha'].iloc[0],
        "Descrição do Defeito": grupo['Descrição do Defeito'].iloc[0],
        "Praetor": grupo['Praetor'].iloc[0],
        "inpeção": grupo['inpeção'].iloc[0],
        "Região": grupo['Região'].iloc[0]
    }

    # Filtrar status
    aberto = grupo[grupo['Status'].str.contains('Aberto', case=False)]['DataVersao']
    andamento = grupo[grupo['Status'].str.contains('Em andamento', case=False)]['DataVersao']
    executado = grupo[grupo['Status'].str.contains('Executado$', case=False)]['DataVersao']
    reaberto = grupo[grupo['Status'].str.contains('Reaberto', case=False)]['DataVersao']
    executado2 = grupo[grupo['Status'].str.contains('Executado 2', case=False)]['DataVersao']
    encerrado_qualidade = grupo[grupo['Status'].str.contains('Encerrado Somente Qualidade e Delegado', case=False)]['DataVersao']

    # Calcular como fração de dia (baseado em horas totais)
    if not aberto.empty and not andamento.empty:
        delta = andamento.values[0] - aberto.values[0]
        tempos['Aberto → Em andamento (fração dia)'] = horas_em_fracao_dia(delta)

    if not andamento.empty and not executado.empty:
        delta = executado.values[0] - andamento.values[0]
        tempos['Em andamento → Executado (fração dia)'] = horas_em_fracao_dia(delta)

    if not reaberto.empty and not executado2.empty:
        delta = executado2.values[0] - reaberto.values[0]
        tempos['Reaberto → Executado 2 (fração dia)'] = horas_em_fracao_dia(delta)

    if not executado.empty and not encerrado_qualidade.empty:
        delta = encerrado_qualidade.values[0] - executado.values[0]
        tempos['Executado → Encerrado Qualidade (fração dia)'] = horas_em_fracao_dia(delta)

    if not executado2.empty and not encerrado_qualidade.empty:
        delta = encerrado_qualidade.values[0] - executado2.values[0]
        tempos['Executado 2 → Encerrado Qualidade (fração dia)'] = horas_em_fracao_dia(delta)

    if not aberto.empty and not encerrado_qualidade.empty:
        delta = encerrado_qualidade.values[0] - aberto.values[0]
        tempos['Aberto → Encerrado Qualidade (fração dia)'] = horas_em_fracao_dia(delta)

    resultados.append(tempos)

# Criar DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Mostrar no terminal
print(df_resultados)

# Salvar em Excel
nome_arquivo = f"tempos_status_praetor_{praetor_escolhido}_excel_horas.xlsx"
df_resultados.to_excel(nome_arquivo, index=False)
print(f"Arquivo salvo como: {nome_arquivo}")
