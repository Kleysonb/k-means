import sys
import csv
import random

# MAIN passando os parametros para o algoritmo
if __name__ == "__main__":

    arquivo_csv = "data/data_abalone.csv"
    k = 3
    atributo1 = 1
    atributo2 = 3
    nome_tabela = "Perfil"

    list_coordenadas = []

    with open(arquivo_csv, 'rb') as ficheiro:
        reader = csv.reader(ficheiro)
        try:
            for linha in reader:
                ponto = [linha[atributo1], linha[atributo2], random.randint(1, k)]
                list_coordenadas.append(ponto)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (arquivo_csv, reader.line_num, e))

    centroide = []
    for index in range(k):
        centroide.append(ponto.index(k))
    for index in range(len(list_coordenadas)):
        print list_coordenadas[index]

    # if len(sys.argv) < 5:
    #     print("Compile assim 'python k-means.py [arquivo.csv] [nome da tabela] [k] [Atributo 1] [Atributo 2] ... [Atributo N]")
    #     exit()
    # else:
    #     arquivo_csv = sys.argv[1]
    #     with open(arquivo_csv, 'rb') as ficheiro:
    #         reader = csv.reader(ficheiro)
    #         try:
    #             for linha in reader:
    #                 print linha
    #         except csv.Error as e:
    #             sys.exit('ficheiro %s, linha %d: %s' % (arquivo_csv, reader.line_num, e))
