from pathlib import Path
import os

# Pasta onde está contido o arquivo executado. Documentação do Path: https://docs.python.org/3.12/library/pathlib.html#basic-use
caminho_arquivo = Path(__file__).parent
itens_comprados = ['Heineken', 'Queijo', 'Cachaca']

# Forma recomendada
with open(caminho_arquivo / 'folder1' / 'folder2' / 'file2.txt', mode='r') as lista_compras2:
    itens_lista = lista_compras2.readlines()

# with open(caminho_arquivo / 'folder1' / 'folder2' / 'file2_new.txt', mode='w') as lista_atual:
#     for item in itens_lista:
#         if not item.replace('\n', '') in itens_comprados:
#             lista_atual.write(item)

# lista_atualizada = []
# for item in itens_lista:
#     if not item.replace('\n', '') in itens_comprados:
#         lista_atualizada.append(item)
#
# with open(caminho_arquivo / 'folder1' / 'folder2' / 'lista_atualizada.txt', mode='w') as lista_atual:
#     lista_atual.writelines(lista_atualizada)
#

# novos_itens = ['cereal', 'farinha lactea']
# itens_quebra = [f'{item}\n' for item in novos_itens]
# with open(caminho_arquivo / 'folder1' / 'folder2' / 'lista_atualizada.txt', mode='a') as novos:
#     novos.writelines(itens_quebra)