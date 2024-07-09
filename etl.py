# Ler um arquivo csv

import csv


def ler_arquivo_csv(nome_do_arquivo: str) -> list[dict]:
    # função para fazer a leitura de um arquivo csv

    lista = []

    with open(nome_do_arquivo, mode="r", encoding= "utf8") as arquivo:
         leitor = csv.DictReader(arquivo)     
         for linha in leitor:
             lista.append(linha)                                                      
    return(lista)




def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:

    # função para filtrar os produtos que foram entregues
    produtos_filtrados = []
    for produtos in lista:
        if produtos.get("entregue") == "True":
         produtos_filtrados.append(produtos)
    return produtos_filtrados


def somar_os_valores_da_lista(lista_dos_produtos_filtrados: list[dict]) -> float:
    # função que soma todos os valores de uma lista
    
    valor_total_dos_produtos = 0
    for produtos in lista_dos_produtos_filtrados:
       valor_total_dos_produtos += float(produtos.get("price"))
         
    return valor_total_dos_produtos


