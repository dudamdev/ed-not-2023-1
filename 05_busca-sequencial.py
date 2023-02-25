def linha():
    print("-" * 100, "\n")

# lista de números
nums = [9, 21, 33, 12, 0, 18, 24, 30, 15, 6, 3, 27]

"""
    Função que realiza uma busca sequencial em uma lista
    procurando por val.
    Se val for encontrado, retorna a posição de val.
    Caso contrário, retorna o valor -1.
"""
def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    # Percorreu toda a lista e não encontrou val: retorna -1
    return -1

# TESTES

# Procurando o valor 15
resultado = busca_sequencial(nums, 15)
print(f"Posição do valor 15 na lista: {resultado}")

# Procurando o valor 20
resultado = busca_sequencial(nums, 20)
print(f"Posição do valor 20 na lista: {resultado}")

# Procurando o valor 33
resultado = busca_sequencial(nums, 33)
print(f"Posição do valor 33 na lista: {resultado}")

linha()

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from time import time

from data.lista_nomes import nomes

# Busca pelo nome EDUARDA
hora_ini = time()
resultado = busca_sequencial(nomes, "EDUARDA")
hora_fim = time()
print(f"Posição do nome Eduarda na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms")

# Busca pelo nome Gabriela
hora_ini = time()
resultado = busca_sequencial(nomes, "GABRIELA")
hora_fim = time()
print(f"Posição do nome Gabriela na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms")

# Busca pelo nome Vanessa
hora_ini = time()
resultado = busca_sequencial(nomes, "VANESSA")
hora_fim = time()
print(f"Posição do nome Vanessa na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms")

# Busca pelo nome Orkutilson
hora_ini = time()
resultado = busca_sequencial(nomes, "ORKUTILSON")
hora_fim = time()
print(f"Posição do nome Orkutilson na lista: {resultado}")
print(f"Tempo gasto: {round((hora_fim-hora_ini) * 1000, 3)} ms")


