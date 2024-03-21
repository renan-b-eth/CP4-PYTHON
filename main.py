import time
import random
import matplotlib.pyplot as plt

#Metodo para geracao de uma lista

def gerar_dados_testes(lista, tamanho_dados, inicio):
    lista = []
    while(inicio < tamanho_dados):
        lista.append(random.randint(0, tamanho_dados))
        inicio = inicio + 1
    return lista

lista2 = []

print(gerar_dados_testes(lista2, 100, 1))
        