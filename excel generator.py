# ESTE FOI O ARQUIVO PYTHON USADO PARA GERAR A PLANILHA DE TRANSIÇÕES DA MT1 E MT2
# A PARTIR DO ARQUIVO JFF DA MT1 E MT2
import xml.etree.ElementTree as ET
import pandas as pd

caminho_arquivo = 'nome do arquivo lido.jff'

tree = ET.parse(caminho_arquivo)
root = tree.getroot()

states = {}
for state in root.iter('state'):
    state_id = state.attrib['id']
    state_name = state.attrib['name']
    states[state_id] = state_name

transicoes = []
for trans in root.iter('transition'):
    origem = states[trans.find('from').text]
    destino = states[trans.find('to').text]

    simbolo_lido = trans.find('read').text or 'ε'
    simbolo_escrito = trans.find('write').text or 'ε'
    movimento = trans.find('move').text or 'ε'

    transicoes.append((origem, simbolo_lido, simbolo_escrito, movimento, destino))

df = pd.DataFrame(transicoes, columns=[
    'Origem', 'Símbolo Lido', 'Símbolo Escrito', 'Movimento', 'Destino'
])

df.to_excel('nome do arquivo gerado.xlsx', index=False)

print("Arquivo Excel gerado com sucesso!")
