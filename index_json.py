from pathlib import Path
import json

data_json = '''
{
    "assinantes": [
        {
            "nome": "André Lucas",
            "sobrenome": "Freitas",
            "idade": 31,
            "estudante": false
        },
        {
            "nome": "Marcelo Moreira",
            "sobrenome": "Franco",
            "idade": 56,
            "estudante": true
        }
    ],
    "atualizacao": "2024-12-01"
}
'''

# Convertendo para Dict
# dado_convertido = json.loads(data_json)
# print(dado_convertido)
#
# Convertendo novamente para JSON
# dado_desconvertido = json.dumps(dado_convertido, ensure_ascii=False, indent=2)
# print(dado_desconvertido)

file_json = Path(__file__).parent / 'jsons' / 'assinantes.json'
with open(file_json, 'r', encoding='utf-8') as f:
    dado_carregado = json.load(f)

with open(Path(__file__).parent / 'jsons' / 'assinantes_atualizacao.json', 'w', encoding='utf-8') as f:
    json.dump(dado_carregado, f, indent=2, ensure_ascii=False)