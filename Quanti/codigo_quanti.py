def verifica_dados(elem_atual, elem_antigo, id):
    for chave, valor in elem_antigo.items():
        if str(elem_atual[chave]) != str(valor):
            isin = id.split('_')[0]
            data = id.split('_')[1]
            dados = {
                'ISIN':[isin],
                'campo_alterado':[chave],
                'valor_antigo':[valor],
                'valor_novo': [elem_atual[chave]],
                'data':[data],
            }
            if os.path.exists('results/serie_valores_substitutos.csv'):
                pd.DataFrame(dados).to_csv('results/serie_valores_substitutos.csv', mode='a', header=False, index=False)
            else:
                pd.DataFrame(dados).to_csv('results/serie_valores_substitutos.csv', index=False)
            elem_antigo[chave] = valor
    return elem_antigo

# Dicionário pode ser consideravelmente grande, no caso de executar com isso em grandes dados
# Fazer um sistema de guardar em arquivos .json, onde é possível verificar as entradas um a um.
df0 = {}


for elem in range(len(arquivos)):
    df1 = pd.read_csv('arquivos_diarios_extraidos/{}'.format(arquivos[elem]))
    df1['ID'] = df1['ISIN'] + '_' + df1['AuM Fund Date']
    df1 = df1.dropna(subset=['ISIN', 'ID'])
    df1.drop_duplicates('ID', keep='last') #perde info porém é para dados entre dias
    for _, elem in df1.iterrows():
        if elem['ID'] in list(df0.keys()):
            df0[elem['ID']] = verifica_dados(elem, df0[elem['ID']], elem['ID'])
        else:
            df0[elem['ID']] = {
                                      'FE Bid':elem['FE Bid'],
                                      'AuM Fund':elem['AuM Fund'],
                                      'AuM Share Class':elem['AuM Share Class'],
                                      'Bid NAV':elem['Bid NAV'],
                                      'Ask NAV':elem['Ask NAV'],
                                      'Valuation NAV':elem['Valuation NAV'],
                                      'NoS Share Class':elem['NoS Share Class'],
                                      'NoS Fund':elem['NoS Fund'],
                                      'FE Offer':elem['FE Offer'],
                                      'FE NAV':elem['FE NAV'],
                                      'FE AUM Fund':elem['FE AUM Fund'],
                                      'FE Generic NAV':elem['FE Generic NAV'],
                                      'Transaction NAV':elem['Transaction NAV'],
                                      'FE Generic NAV':elem['FE Generic NAV'],
                                      'FE NAV':elem['FE NAV'],
                                      'Transaction NAV':elem['Transaction NAV']
            }
    
