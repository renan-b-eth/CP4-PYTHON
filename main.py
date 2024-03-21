import time
import random
import matplotlib.pyplot as plt
from algoritmos import algoritmos
#import Ordernacao 

#ord = algoritmos.Ordernacao() # instanciar o objeto

#Metodo para geracao de uma lista

def gerar_dados_testes(lista, tamanho_dados, inicio):
    lista = []
    while(inicio < tamanho_dados):
        lista.append(random.randint(0, tamanho_dados))
        inicio = inicio + 1
    return lista

lista2 = []

lista3 = gerar_dados_testes(lista2, 10000, 1)

print(lista3)

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] ## troca de posição
    return lista


#metodo para definir tempo_Execucao
def medir_tempo_execucao(algoritmo, lista):
    inicio = time.time() ### define o tempo inicial
    algoritmo(lista)     ### algoritmo sendo executado
    fim = time.time()    ### tempo final
    return fim - inicio  ### calcula o tempo total de execução

tempo_bubbler = medir_tempo_execucao(bubble_sort, lista3)
tempo_selection_sort = 1
tempo_insertion_sort = 2
tempo_mergeSort = 3
tempo_quickSort = 5 

#criacao do dicionario com os dados
tempos = {'bubble_sort': tempo_bubbler,
          'selection_sort': tempo_selection_sort,
          'insertion_sort': tempo_insertion_sort,
          'mergeSort': tempo_mergeSort,
          'quickSort': tempo_quickSort}

print(tempos["bubble_sort"])

def gerar_graficos(tempo):
    plt.plot(tempos['bubble_sort'])
    plt.show()
    return tempo

gerar_graficos(tempos)

        