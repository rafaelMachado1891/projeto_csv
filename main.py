from etl import ler_arquivo_csv, somar_os_valores_da_lista, filtrar_produtos_entregues

caminho_do_arquivo = "arquivo.csv"


arquivo = ler_arquivo_csv(caminho_do_arquivo)

print(arquivo)