
import random
import test_ordenacao
class Teste_Busca:

    #Busca por um elemento que está presente no vetor.
    #Busca por um elemento que não está presente no vetor.
    #Busca em um vetor vazio.
    #Busca em um vetor com um único elemento.


    test_ordenacao = test_ordenacao.Test_Ordenacao
    #tamanho da lista
    tamanho_lista = 1000
      
    def gerar_dados_testes(lista, tamanho_dados, inicio):
        lista = []
        while(inicio < tamanho_dados):
            lista.append(random.randint(0, tamanho_dados))
            inicio = inicio + 1
        return lista

    lista =  []
    lista2 = gerar_dados_testes(lista,tamanho_lista,1)


    def buscar_elemento(lista, elemento):
        posicoes = []
        for elemento in elemento:
            if elemento in lista:
                posicoes.append(lista.index(elemento))
        return posicoes
    
    def buscar_elemento_nao_vetor(lista, elemento):
        if elemento not in lista:
            print(str(elemento) + " nao esta na lista")
        else:
            print(str(elemento) + " esta na lista")
        return ""
    
    def buscar_elemento_vetor_vazio(lista):
        if not lista:
            print("A lista esta vazia")
        else:
            print("A lista nao esta vazia")
        return ""
    
    def buscar_elemento_vetor_unico(vetor, elemento):
        if len(vetor) == 1:
            if vetor[0] == elemento:
                return True
            else:
                return False
        else:
            return "O vetor nao contém um único elemento."

    #pode alterar o final do vetor para até o 7
    posicao_vetores = buscar_elemento(lista2, test_ordenacao.vetor)



    print("OS VALORES DO VETOR: " + str(test_ordenacao.vetor) + " SE ENCONTRAM NOS SEGUINTES INDEX DA LISTA GERADA: " + str(posicao_vetores))
    print("")
    i=0
    while(i<len(posicao_vetores)):
        #aqui mostra os numeros encontrados nas seguintes posições
        print("POSICAO INDEX " + str(posicao_vetores[i]) + " FOI ENCONTRADO O SEGUINTE VALOR:  " + str(lista2[posicao_vetores[i]]))
        i = i + 1
    print("")
    elemento = 55564654   # numero exorbitante para procurar um numero na lista para dar erro
    print(buscar_elemento_nao_vetor(lista2, elemento))

    #colocar um valor depois 
    lista3 = test_ordenacao.vetor4 #vetor4 é o vazio.
    print(buscar_elemento_vetor_vazio(lista3))

    vetor_unico = test_ordenacao.vetor5 # aqui usa o vetor5
    elemento_busca = 5 # aqui o numero certo é 42
    
    print(buscar_elemento_vetor_unico(vetor_unico, elemento_busca))
    
