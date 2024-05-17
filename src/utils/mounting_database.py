import os
import json

# Diretório contendo os arquivos JSON
diretorio = '../database/'

# Lista para armazenar os dados combinados
dados_combinados = []

# Listar todos os arquivos JSON no diretório
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.json'):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        # Ler o conteúdo do arquivo JSON e armazenar na lista de dados combinados
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_arquivo = json.load(arquivo)
            print(dados_arquivo)
            dados_combinados.append(dados_arquivo)

# Escrever os dados combinados em um novo arquivo JSON
caminho_saida = 'database.json'
with open(caminho_saida, 'w') as arquivo_saida:
    json.dump(dados_combinados, arquivo_saida, indent=4)

print("Arquivos JSON combinados com sucesso!")