# Ler um arquivo csv

import csv

caminho_do_arquivo = "arquivo.csv"

def ler_arquivo_csv(nome_do_arquivo: str) -> list[dict]:

    lista = []

    with open(nome_do_arquivo, mode="r", encoding= "utf8") as arquivo:
         leitor = csv.DictReader(arquivo)     
         for linha in leitor:
             lista.append(linha)                                                      
    return(lista)

print(ler_arquivo_csv(caminho_do_arquivo))