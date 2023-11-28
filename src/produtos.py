import pandas as pd

tabela = pd.read_excel('produtos.xlsx')

produtos = tabela.loc[tabela['Tipo']=='Produto']
servicos = tabela.loc[tabela['Tipo']=='Serviço']
print(f'A tabela possui {produtos.shape[0]} produtos e {servicos.shape[0]} serviços')

tabela.loc[tabela['Tipo']=='Serviço', 'Multiplicador Imposto'] = 1.5
tabela['Preço Base Reais'] = tabela['Multiplicador Imposto']*tabela['Preço Base Original']
display(tabela)
tabela.to_excel('produtos_15.xlsx', index=False)
