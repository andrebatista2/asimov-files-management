import xml.dom.minidom
from pathlib import Path

file_location = Path(__file__).parent / 'xmls'
domtree = xml.dom.minidom.parse(str(file_location / 'file.xml'))

groups = domtree.documentElement
livros = groups.getElementsByTagName('book')

for livro in livros:
    titulo = livro.getElementsByTagName('title')[0].childNodes[0].nodeValue
    autor = livro.getElementsByTagName('author')[0].childNodes[0].nodeValue
    print(f"{autor} - {titulo}")

livros[0].getElementsByTagName('author')[0].childNodes[0].nodeValue = 'Batista, André'
with open(file_location / 'file_updated.xml', 'w') as file:
    domtree.writexml(file)