import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('../../Quantum - Hackathon Engenharia de Dados/Quanti/Lote Inicial/LoteInicial/LoteInicial.csv', nrows=1048575)

# Ordenação pelo 'ID' e pela 'Data' em ordem decrescente
df_sorted = df.sort_values(by=['ISIN', 'General Reference Date'], ascending=[True, False])

# Agrupamento por 'ID' e obtenção da primeira linha de cada grupo (último dia registrado)
df_grouped = df_sorted.groupby('ISIN').head(1).reset_index(drop=True)

# Exibindo o resultado
print(df_grouped)

df_grouped.to_csv(('arquivo_finalizado.csv'), index=False)