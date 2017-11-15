import sys
import csv
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors


def calcularDistacia(x1, y1, x2, y2):
    #return ((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2)**0.5
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def gerarMatriz(centroide, list_coordenadas):
    alteracoes = False
    for ponto in range(len(list_coordenadas)):
        menor = 0
        centro = list_coordenadas[ponto][2]
        for k in range(len(centroide)):
            if(k == 0):
                menor = calcularDistacia(centroide[k][0], centroide[k][1], list_coordenadas[ponto][0], list_coordenadas[ponto][1])
                centro = k+1
            else:
                aux = calcularDistacia(centroide[k][0], centroide[k][1], list_coordenadas[ponto][0], list_coordenadas[ponto][1])
                if(aux < menor):
                    menor = aux
                    centro = k+1
        #print str(menor) + " : " + str(centro)
        #Recebendo o novo centroide
        if(centro != list_coordenadas[ponto][2]):
            list_coordenadas[ponto][2] = centro
            alteracoes = True

    refinarCentroide(centroide, list_coordenadas)
    return alteracoes

def plota_dispersao(list_coordenadas):
    fig = plt.figure()

    ax1 = fig.add_subplot(121)
    x = []
    y = []
    for index in range(len(list_coordenadas)):
        if(list_coordenadas[index][2] == 1):
            x.append(list_coordenadas[index][0])
            y.append(list_coordenadas[index][1])
    ax1.scatter(x, y, color = "blue", s = 3, edgecolor='none')
    ax1.set_aspect(1. / ax1.get_data_ratio())

    ax2 = fig.add_subplot(121)
    x1 = []
    y1 = []
    for index in range(len(list_coordenadas)):
        if (list_coordenadas[index][2] == 2):
            x1.append(list_coordenadas[index][0])
            y1.append(list_coordenadas[index][1])
    ax2.scatter(x1, y1, color="red", s=3, edgecolor='none')
    ax2.set_aspect(1. / ax2.get_data_ratio())


    ax3 = fig.add_subplot(121)
    x2 = []
    y2 = []
    for index in range(len(list_coordenadas)):
        if (list_coordenadas[index][2] == 3):
            x2.append(list_coordenadas[index][0])
            y2.append(list_coordenadas[index][1])
    ax3.scatter(x2, y2, color="green", s=3, edgecolor='none')
    ax3.set_aspect(1. / ax3.get_data_ratio())

    plt.show()

def refinarCentroide(centroide, list_coordenadas):
    for i in range(len(centroide)):
        cont = 0
        somaX = 0
        somaY = 0
        for j in range(len(list_coordenadas)):
            if (list_coordenadas[j][2] == i+1):
                somaX += list_coordenadas[j][0]
                somaY += list_coordenadas[j][1]
                cont += 1
        centroide[i][0] = somaX/cont
        centroide[i][1] = somaY/cont

    print "Novos Centroides:"
    for index in range(len(centroide)):
        print centroide[index]

# MAIN passando os parametros para o algoritmo
if __name__ == "__main__":

    arquivo_csv = "data/data_cpu.csv"
    k = 3
    atributo1 = 7
    atributo2 = 8
    nome_tabela = "Perfil"

    list_coordenadas = []

    #Lendo o arquivo
    with open(arquivo_csv, 'rb') as ficheiro:
        reader = csv.reader(ficheiro)
        try:
            for linha in reader:
                #Criando tabela com os atributos informados e definindo um cluster qualquer possivel
                ponto = [float(linha[atributo1]), float(linha[atributo2]), random.randint(1, k)]
                list_coordenadas.append(ponto)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (arquivo_csv, reader.line_num, e))

    centroide = []
    aux = len(list_coordenadas) - 1
    for index in range(k):
        #Escolhendo k centroides aleatorios
        aleatorio = random.randint(0, aux)
        #Para que cada centroide possua um cluster diferente
        list_coordenadas[aleatorio][2] = index+1
        centroide.append(list_coordenadas[aleatorio])
    for index in range(len(centroide)):
        print centroide[index]


    plota_dispersao(list_coordenadas)

    alteracoes = gerarMatriz(centroide, list_coordenadas)

    while(alteracoes):
        alteracoes = gerarMatriz(centroide, list_coordenadas)

        plota_dispersao(list_coordenadas)
    print "Finalizado"

    # for index in range(len(list_coordenadas)):
    #     print list_coordenadas[index]

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
