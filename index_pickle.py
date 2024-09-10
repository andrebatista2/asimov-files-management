import pickle
from pathlib import Path

current = Path(__file__).parent / 'pickles'

lista = [1, 2, 3, 4, 5, 6]
dicionario = {'a': 1, 'b': 2}

# wb - Escrevendo um arquivo em bytes (linguagem de máquina)
with open(current / 'lista.pickle', 'wb') as file:
    pickle.dump(lista, file)

with open(current / 'dicionario.pickle', 'wb') as file:
    pickle.dump(dicionario, file)

with open(current / 'lista.pickle', 'rb') as file:
    lista_lida = pickle.load(file)
    print(lista_lida)

with open(current / 'dicionario.pickle', 'rb') as file:
    dict_lido = pickle.load(file)
    print(dict_lido)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def quem_yo_soy(self):
        print(f'{self.nome} {self.idade}')


inst_nome = Pessoa('João', 12)
# inst_nome.quem_yo_soy()

with open(current / 'classe_serializada.pickle', 'wb') as file:
    pickle.dump(inst_nome, file)

with open(current / 'classe_serializada.pickle', 'rb') as file:
    obj_pessoa = pickle.load(file)

obj_pessoa.quem_yo_soy()