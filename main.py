import time
import random
import matplotlib.pyplot as plt
import algoritmos.testes 
import algoritmos.algoritmos
from algoritmos.algoritmos.ordenacao import Ordernacao
from algoritmos.testes.test_busca import Teste_Busca

class Main:

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

    lista3 = gerar_dados_testes(lista2, 10000, 1)

    #print(lista3)
    #print(ordenacao.bubble_sort(lista3))
    #print(ordenacao.mergeSort(lista3))
    #print(ordenacao.insertion_sort(lista3))
    #print(ordenacao.selection_sort(lista3))



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



    def gerar_graficos(tempos):
        x = ["TEMPO BUBBLE", "TEMPO SELECTION", "TEMPO INSERTION", "TEMPO MERGE"]
        y = [tempos["bubble_sort"], tempos["selection_sort"], tempos["insertion_sort"], tempos["mergeSort"]]

        fig, ax = plt.subplots()
        bars = ax.bar(x=x, height=y)
        
        # Adicionando rótulos de valor nas barras
        for bar in bars:
            yval = bar.get_height()
            yval2 = round(yval,3)
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, float(yval2), va='bottom') # Alinhamento vertical 'bottom'
        
        plt.title("Tempo de execução dos metodos de ordenação")
        plt.show()
        
        return bars

    gerar_graficos(tempos)