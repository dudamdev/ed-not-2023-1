"""
    ALGORITMO DE BUSCA BINÁRIA
    Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
    e um valor de busca, divide a lista em duas metades
    procurando pelo valor de busca apenas na metade onde
    o valor poderia estar. Novas subdivisões são feitas
    até que se encontre o valor de busca ou que reste
    apenas uma sublista vazia, quando então se conclui
    que o valor de busca não existe na lista. 
"""

comps = 0   # Conta o número de comparações

def busca_binaria(lista, val):
    global comps
    comps = 0 

    ini = 0                 # Início da lista
    fim = len(lista) - 1    # Fim da lista

    while ini <= fim:
        meio = (ini + fim) // 2     # // = Divisão inteira

        # O valor de busca foi encontrado
        # Retorna a posição
        if lista[meio] == val: 
            comps += 1
            return meio
        elif val < lista[meio]:
            comps += 2
            fim = meio - 1
        else: # val > lista[meio]:
            comps += 2
            ini = meio + 1

    return -1   # Valor não existe na lista

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from time import time

from data.lista_nomes import nomes

# Busca pelo nome EDUARDA
hora_ini = time()
resultado = busca_binaria(nomes, "EDUARDA")
hora_fim = time()
print(f"Posição do nome Eduarda na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms, comparações: {comps}")

# Busca pelo nome Gabriela
hora_ini = time()
resultado = busca_binaria(nomes, "GABRIELA")
hora_fim = time()
print(f"Posição do nome Gabriela na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms, comparações: {comps}")

# Busca pelo nome Vanessa
hora_ini = time()
resultado = busca_binaria(nomes, "VANESSA")
hora_fim = time()
print(f"Posição do nome Vanessa na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms, comparações: {comps}")

# Busca pelo nome Orkutilson
hora_ini = time()
resultado = busca_binaria(nomes, "ORKUTILSON")
hora_fim = time()
print(f"Posição do nome Orkutilson na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms, comparações: {comps}")

# Busca pelo nome Aarao
hora_ini = time()
resultado = busca_binaria(nomes, "AARAO")
hora_fim = time()
print(f"Posição do nome Aarao na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms, comparações: {comps}")