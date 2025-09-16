import pandas as pd

df = pd.read_excel('HistoricoVersoes (5).xlsx')
df.head(10)
df.columns = df.columns.str.strip()
df['DataVersao'] = pd.to_datetime(df['DataVersao'])
df['Status'] = df['Status'].str.lower()
df = df.dropna(how='all')



resultados = []

for id_val in df['ID'].unique():
    subset = df[df['ID'] == id_val]

    andamento = subset[subset['Status'] == 'em andamento']
    encerrado = subset[subset['Status'] == 'encerrado']
    reaberto = subset[subset['Status'] == 'reaberto']
    encerrado2 = subset[subset['Status'] == 'encerrado 2']

    tempo1 = None
    tempo2 = None

    if not andamento.empty and not encerrado.empty:
        tempo1 = encerrado.iloc[0]['DataVersao'] - andamento.iloc[0]['DataVersao']

    if not reaberto.empty and not encerrado2.empty:
        tempo2 = encerrado2.iloc[0]['DataVersao'] - reaberto.iloc[0]['DataVersao']

    resultados.append({
        'ID': id_val,
        'Tempo_Em_Andamento_Encerrado': tempo1,
        'Tempo_Reaberto_Encerrado2': tempo2
    })

resultado_df = pd.DataFrame(resultados)
print(resultado_df)
resultado_df.to_excel('tempos_calculados.xlsx', index=False)


print(df.columns)

print(df)