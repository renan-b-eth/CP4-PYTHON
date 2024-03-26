# Integrantes

- Keven Ike Pereira da Silva - 553215
- Lucas Alcântara Carvalho - 95111
- Renan Bezerra dos Santos - 553228

# Biblioteca de Algoritmos em Python

É uma biblioteca customizada em Python que contém implementações de algoritmos de busca e ordenação. Os teste estão localizados no diretório algoritmos/algoritmos.

## Algoritmos de Busca

- **Busca Sequencial:** Implementa busca sequencial em uma lista.
- **Busca Binária:** Implementa busca binária em uma lista ordenada.

## Algoritmos de Ordenação

- **Bubble Sort:** Implementa o algoritmo para ordenação de uma lista.
- **Selection Sort:** Implementa o algoritmo para ordenação de uma lista.
- **Insertion Sort:** Implementa o algoritmo para ordenação de uma lista.
- **Merge Sort:** Implementa o algoritmo para ordenação de uma lista.


## Testes

A biblioteca inclui testes para garantir o funcionamento correto dos algoritmos. Os testes estão localizados no diretório algoritmos/testes.

### Testes de Ordenação (ordenacao.py)

O módulo test_ordenacao.py contém testes para os algoritmos de ordenação:

- Vetor ordenado crescente
- Vetor não ordenado
- Vetor ordenado descrescente
- Vetor vazio
- Vetor com um único elemento
- Vetor com elementos repetidos
- Vetor com elementos negativos

### Testes de Busca (busca.py)

O módulo test_busca.py contém testes para os algoritmos de busca:

- Busca por um elemento que está presente no vetor
- Busca por um elemento que não está presente no vetor
- Busca em um vetor vazio
- Busca em um vetor com um único elemento

___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
## Análise de Desempenho e Relatórios de Teste (main.py).

Para analisar o desempenho dos algoritmos de ordenação.

- **Importação de Módulos Necessários**: Módulos importantes, `time`, `random`, `matplotlib.pyplot` e os módulos de ordenação e busca da nossa biblioteca.

- **Geração de Dados de Teste**: Criação de listas de diferentes tamanhos.

- **Medição de Tempo de Execução**: Para cada lista, medimos o tempo de execução de cada algoritmo de ordenação. Utilizando a função `time.time()` para obter o tempo da execução do algoritmo.

- **Armazenamento de Resultados**: Armazenamos os resultado em um dicionário, onde as chaves são os nomes dos algoritmos e os valores são listas dos tempos de execução correspondentes a cada tamanho de lista de teste.

- **Geração de Gráfico**: Utilizamos `matplotlib.pyplot` para gerar um gráfico que compara o tempo de execução dos algoritmos em função do tamanho da lista de teste. O gráfico mostra o tempo de execução de cada algoritmo em diferentes tamanhos de listas.

- **Identificação do Algoritmo Campeão**: Analisamos o gráfico para determinar qual algoritmo teve o melhor tempo de execução para os diferentes tamanhos de lista.
