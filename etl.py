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




def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    produtos_filtrados = []
    for produtos in lista:
        if produtos.get("entregue") == "True":
         produtos_filtrados.append(produtos)
    return produtos_filtrados

produtos_csv = ler_arquivo_csv(caminho_do_arquivo)
produtos_entregues = filtrar_produtos_entregues(produtos_csv)
print(produtos_entregues)


