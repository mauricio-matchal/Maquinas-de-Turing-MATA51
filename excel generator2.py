import pandas as pd
import xml.etree.ElementTree as ET

arquivo_jff = "nome do arquivo lido.jff"

tree = ET.parse(arquivo_jff)
root = tree.getroot()

id_para_nome = {}
for state in root.find("automaton").findall("state"):
    state_id = state.attrib["id"]
    state_name = state.attrib["name"]
    id_para_nome[state_id] = state_name

transicoes = []

for t in root.find("automaton").findall("transition"):
    de_id = t.findtext("from")
    para_id = t.findtext("to")
    de_nome = id_para_nome.get(de_id, f"q{de_id}")
    para_nome = id_para_nome.get(para_id, f"q{para_id}")
    
    fita_data = {}
    for i in range(1, 4):
        ler = t.find(f"read[@tape='{i}']")
        escrever = t.find(f"write[@tape='{i}']")
        mover = t.find(f"move[@tape='{i}']")

        fita_data[f"Ler{i}"] = ler.text if ler is not None else ""
        fita_data[f"Escrever{i}"] = escrever.text if escrever is not None else ""
        fita_data[f"Mover{i}"] = mover.text if mover is not None else ""

    transicoes.append({
        "De": de_nome,
        "Para": para_nome,
        **fita_data
    })

df = pd.DataFrame(transicoes)

df.to_excel("nome do arquivo gerado.xlsx", index=False)

print("Excel gerado com sucesso")
