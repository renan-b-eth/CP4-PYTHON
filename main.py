import time
import random
import matplotlib.pyplot as plt
import algoritmos.testes 
import algoritmos.algoritmos
from algoritmos.algoritmos.ordenacao import Ordernacao
from algoritmos.testes.test_busca import Teste_Busca

ordenacao = Ordernacao
teste = Teste_Busca


#Metodo para geracao de uma lista

def gerar_dados_testes(lista, tamanho_dados, inicio):
    lista = []
    while(inicio < tamanho_dados):
        lista.append(random.randint(0, tamanho_dados))
        inicio = inicio + 1
    return lista

lista2 = []

lista3 = gerar_dados_testes(lista2, 1000, 1)

#print(lista3)
#print(ordenacao.bubble_sort(lista3))


#metodo para definir tempo_Execucao
def medir_tempo_execucao(algoritmo, lista):
    inicio = time.time() ### define o tempo inicial
    algoritmo(lista)     ### algoritmo sendo executado
    fim = time.time()    ### tempo final
    return fim - inicio  ### calcula o tempo total de execução

tempo_bubbler = medir_tempo_execucao(ordenacao.bubble_sort, lista3)
tempo_selection_sort = medir_tempo_execucao(ordenacao.selection_sort, lista3)
tempo_insertion_sort = medir_tempo_execucao(ordenacao.insertion_sort, lista3)
tempo_mergeSort = medir_tempo_execucao(ordenacao.mergeSort, lista3)
#tempo_quickSort = medir_tempo_execucao(ordenacao.quickSort, lista3)

#criacao do dicionario com os dados
tempos = {'bubble_sort': tempo_bubbler,
          'selection_sort': tempo_selection_sort,
          'insertion_sort': tempo_insertion_sort,
          'mergeSort': tempo_mergeSort
          #'quickSort': tempo_quickSort
          }

print(tempos["bubble_sort"])
print(tempos["selection_sort"])
print(tempos["insertion_sort"])
print(tempos["mergeSort"])
#print(tempos["quickSort"])



def gerar_graficos(tempo):
    plt.plot(tempos['bubble_sort'])
    plt.show()

    return tempo

#gerar_graficos(tempos)

