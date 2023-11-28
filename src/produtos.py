import pandas as pd

tabela = pd.read_excel('produtos.xlsx')
tabela.loc[tabela['Tipo']=='Serviço', 'Multiplicador de Imposto'] = 1.5
tabela['Preço Base Reais'] = tabela['Multiplicador de Imposto']*tabela['Preço Base Original']
#display(tabela)
tabela.to_excel('produtos_15.xlsx', index=False)