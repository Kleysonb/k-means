import sys
import csv
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors


def calcularDistacia(x1, y1, x2, y2):
    #return ((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2)**0.5
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def euclidiana(ponto, centroide):
    return ((ponto[0]-centroide[0])**2+(ponto[1]-centroide[1])**2+(ponto[2]-centroide[2])**2+(ponto[3]-centroide[3])**2+
    (ponto[4]-centroide[4])**2+(ponto[5]-centroide[5])**2+(ponto[6]-centroide[6])**2+(ponto[7]-centroide[7])**2+(ponto[8]-centroide[8])**2) ** 0.5

def gerarMatriz(centroide, list_coordenadas):
    alteracoes = False
    for ponto in range(len(list_coordenadas)):
        menor = 0
        centro = list_coordenadas[ponto][2]
        for k in range(len(centroide)):
            if(k == 0):
                #menor = calcularDistacia(centroide[k][0], centroide[k][1], list_coordenadas[ponto][0], list_coordenadas[ponto][1])
                menor = euclidiana(list_coordenadas[ponto], centroide[k])
                centro = k+1
            else:
                #aux = calcularDistacia(centroide[k][0], centroide[k][1], list_coordenadas[ponto][0], list_coordenadas[ponto][1])
                aux = euclidiana(list_coordenadas[ponto], centroide[k])
                if(aux < menor):
                    menor = aux
                    centro = k+1
        #print str(menor) + " : " + str(centro)
        #Recebendo o novo centroide
        if(centro != list_coordenadas[ponto][9]):
            list_coordenadas[ponto][9] = centro
            alteracoes = True

    refinarCentroide(centroide, list_coordenadas)
    return alteracoes

def plota_dispersao(list_coordenadas, centroide):
    fig = plt.figure()

    ax1 = fig.add_subplot(121)
    x = []
    y = []
    for index in range(len(list_coordenadas)):
        if(list_coordenadas[index][9] == 1):
            x.append(list_coordenadas[index][2])
            y.append(list_coordenadas[index][5])
    ax1.scatter(x, y, color = "blue", s = 6, edgecolor='none')
    ax1.set_aspect(1. / ax1.get_data_ratio())

    ax3 = fig.add_subplot(121)
    x3 = []
    y3 = []
    x3.append(centroide[0][2])
    y3.append(centroide[0][5])
    ax3.scatter(x3, y3, color="blue", s=30, edgecolor='none')
    ax3.set_aspect(1. / ax1.get_data_ratio())

    ax2 = fig.add_subplot(121)
    x1 = []
    y1 = []
    for index in range(len(list_coordenadas)):
        if (list_coordenadas[index][9] == 2):
            x1.append(list_coordenadas[index][2])
            y1.append(list_coordenadas[index][5])
    ax2.scatter(x1, y1, color="red", s=6, edgecolor='none')
    ax2.set_aspect(1. / ax2.get_data_ratio())

    ax4 = fig.add_subplot(121)
    x4 = []
    y4 = []
    x4.append(centroide[1][2])
    y4.append(centroide[1][5])
    ax4.scatter(x4, y4, color="red", s=30, edgecolor='none')
    ax4.set_aspect(1. / ax1.get_data_ratio())

    plt.show()

def refinarCentroide(centroide, list_coordenadas):
    print "Refinando Centroides"
    for i in range(len(centroide)):
        cont = 0
        atributo1 = 0
        atributo2 = 0
        atributo3 = 0
        atributo4 = 0
        atributo5 = 0
        atributo6 = 0
        atributo7 = 0
        atributo8 = 0
        atributo9 = 0

        for j in range(len(list_coordenadas)):
            if (list_coordenadas[j][9] == i+1):
                atributo1 += list_coordenadas[j][0]
                atributo2 += list_coordenadas[j][1]
                atributo3 += list_coordenadas[j][2]
                atributo4 += list_coordenadas[j][3]
                atributo5 += list_coordenadas[j][4]
                atributo6 += list_coordenadas[j][5]
                atributo7 += list_coordenadas[j][6]
                atributo8 += list_coordenadas[j][7]
                atributo9 += list_coordenadas[j][8]
                cont += 1
        centroide[i][0] = atributo1/cont
        centroide[i][1] = atributo2/cont
        centroide[i][2] = atributo3/cont
        centroide[i][3] = atributo4/cont
        centroide[i][4] = atributo5/cont
        centroide[i][5] = atributo6/cont
        centroide[i][6] = atributo7/cont
        centroide[i][7] = atributo8/cont
        centroide[i][8] = atributo9/cont


    print "Novos Centroides:"
    for index in range(len(centroide)):
        print centroide[index]

def acerto(resultado, list_coordenadas):

    classe1 = 0
    classe2 = 0
    classe3 = 0
    classe4 = 0

    benigno = 444
    maligno = 239

    for index in range(len(list_coordenadas)):
        if (resultado[index] == 1 and list_coordenadas[index][9] == 1):
            classe1+=1
        elif (resultado[index] == 2 and list_coordenadas[index][9] == 2):
            classe2+=1

    for index in range(len(list_coordenadas)):
        if (resultado[index] == 1 and list_coordenadas[index][9] == 2):
            classe3+=1
        elif (resultado[index] == 2 and list_coordenadas[index][9] == 1):
            classe4+=1

    b = 0
    m = 0
    if(classe1 > classe3):
        if (classe1 > classe2):
            print "Benigno: " + str(classe1)
            print "Maligno: " + str(classe2)
            b = abs(classe1 - benigno)
            m = abs(classe2 - maligno)
        else:
            print "Benigno: " + str(classe2)
            print "Maligno: " + str(classe1)
            b = abs(classe2 - benigno)
            m = abs(classe1 - maligno)
    else:
        if(classe3 > classe4):
            print "Benigno: " + str(classe3)
            print "Maligno: " + str(classe4)
            b = abs(classe3 - benigno)
            m = abs(classe4 - maligno)
        else:
            print "Benigno: " + str(classe3)
            print "Maligno: " + str(classe4)
            b = abs(classe4 - benigno)
            m = abs(classe3 - maligno)

    b = (b*100)/benigno
    m = (m*100)/maligno

    print "Taxa de Erro Benigno: " + str(b) + "%"
    print "Taxa de Erro Maligno: " + str(m) + "%"

# MAIN passando os parametros para o algoritmo
if __name__ == "__main__":

    arquivo_csv = "data/breast-cancer-wisconsin.csv"
    k = 2
    nome_tabela = "Classificacao"

    list_coordenadas = []
    resultado = []

    #Lendo o arquivo
    with open(arquivo_csv, 'rb') as ficheiro:
        reader = csv.reader(ficheiro)
        try:
            for linha in reader:
                #Criando tabela com os atributos informados e definindo um cluster qualquer possivel
                ponto = [float(linha[1]), float(linha[2]), float(linha[3]), float(linha[4]), float(linha[5]), float(linha[6]), 
                float(linha[7]), float(linha[8]), float(linha[9]), random.randint(1, 2)]
                #print (ponto)
                if(linha[10] == "2"):
                    #Benigno
                    resultado.append(1)
                else:
                    #Maligno
                    resultado.append(2)
                list_coordenadas.append(ponto)
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (arquivo_csv, reader.line_num, e))

    centroide = []
    aux = len(list_coordenadas) - 1
    for index in range(k):
        #Escolhendo k centroides aleatorios
        aleatorio = random.randint(0, aux)
        #Para que cada centroide possua um cluster diferente
        list_coordenadas[aleatorio][9] = index+1
        centroide.append(list_coordenadas[aleatorio])
    for index in range(len(centroide)):
        print centroide[index]

    
    #plota_dispersao(list_coordenadas, centroide)
    
    
    alteracoes = gerarMatriz(centroide, list_coordenadas)
    

    while(alteracoes):
        alteracoes = gerarMatriz(centroide, list_coordenadas)
        #plota_dispersao(list_coordenadas, centroide)
    plota_dispersao(list_coordenadas, centroide)

    acerto(resultado, list_coordenadas)

    print "Finalizado"

