# Dataframe criado para ler as colunas no arquivo 'colunas_especificas.txt'


import pandas as pd


# Ler o arquivo CSV do Quali 
csv_file_path = '/home/luis/Documents/puc-rj/Quali/Arquivos Diários/Quali_20240601.csv'
df = pd.read_csv(csv_file_path, nrows=1000)

# Criando uma lista com as colunas especificadas
with open('/home/luis/Documents/puc-rj/Quali/colunas_especificas.txt', 'r') as file:
    lista = [linha.strip() for linha in file]

# dataframe com as colunas especificadas
df_quali = df[lista]


print(df_quali)
