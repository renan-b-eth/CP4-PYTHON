
import random
import test_ordenacao
class Teste_Busca:

    #Busca por um elemento que está presente no vetor.
    #Busca por um elemento que não está presente no vetor.
    #Busca em um vetor vazio.
    #Busca em um vetor com um único elemento.


    test_ordenacao = test_ordenacao.Test_Ordenacao

      
    def gerar_dados_testes(lista, tamanho_dados, inicio):
        lista = []
        while(inicio < tamanho_dados):
            lista.append(random.randint(0, tamanho_dados))
            inicio = inicio + 1
        return lista

    lista =  []
    lista2 = gerar_dados_testes(lista,1000,1)


    def buscar_elemento(lista, elemento):
        posicoes = []
        for elemento in elemento:
            if elemento in lista:
                posicoes.append(lista.index(elemento))
        return posicoes
    
    def buscar_elemento_nao_vetor(self):
        return print("oi")
    
    def buscar_elemento_vetor_vazio(self):
        return print("oi")
    
    def buscar_elemento_vetor_unico(self):
        return print("oi")

    #pode alterar o final do vetor para até o 7
    posicao_vetores = buscar_elemento(lista2, test_ordenacao.vetor5)



    print("OS VALORES DO VETOR: " + str(test_ordenacao.vetor5) + " SE ENCONTRAM NOS SEGUINTES INDEX DA LISTA GERADA: " + str(posicao_vetores))
    i=0
    while(i<len(posicao_vetores)):
        #aqui mostra os numeros encontrados nas seguintes posições
        print("POSICAO INDEX " + str(posicao_vetores[i]) + " FOI ENCONTRADO O SEGUINTE VALOR:  " + str(lista2[posicao_vetores[i]]))
        i = i + 1


    
