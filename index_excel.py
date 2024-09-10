from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent / 'planilhas'
tabela_clientes = pd.read_excel(pasta_atual / 'clientes.xlsx')
# print(tabela_clientes.head(10))  # Abre os 10 primeiros registros

tabela_clientes_sc = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='SC')  # Abre uma aba de planilha específica. Index_col remove uma das colunas do DataFrame. Usecols exibe apenas as colunas especificadas, thousands = quebra de milhares
tabela_clientes_rs = pd.read_excel(pasta_atual / 'clientes.xlsx', sheet_name='RS')  # Abre uma aba de planilha específica. Index_col remove uma das colunas do DataFrame. Usecols exibe apenas as colunas especificadas, thousands = quebra de milhares

# Salva os dados do DataFrame em um arquivo Excel
# tabela_clientes_sc.to_excel(pasta_atual / 'clientes_copia.xlsx')

with pd.ExcelWriter(pasta_atual / 'clientes_copia.xlsx') as nova_planilha:
    tabela_clientes_rs.to_excel(nova_planilha, 'Clientes RS', index=False)
    tabela_clientes_sc.to_excel(nova_planilha, 'Clientes SC', index=False)