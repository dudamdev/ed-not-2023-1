"""
    Função que implementa o algoritmo Quick Sort de forma ITERATIVA
"""
# Variáveis de estatística
passadas = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):

    global passadas, comps, trocas

    if fim is None: fim = len(lista) - 1

    # Cria uma lista auxiliar
    tamanho = fim - ini + 1
    aux = [None] * tamanho
  
    # Inicializa a posição da lista auxiliar
    pos = -1
  
    # Coloca os valores iniciais de ini e fim na lista auxiliar
    pos = pos + 1
    aux[pos] = ini
    pos = pos + 1
    aux[pos] = fim
  
    # Continua retirando valores da lista auxiliar enquanto
    # ela não estiver vazia
    while pos >= 0:
        passadas += 1

        # print(aux)
  
        # Retira fim e início
        fim = aux[pos]
        pos = pos - 1
        ini = aux[pos]
        pos = pos - 1
  
        # Coloca o pivô em sua posição correta na lista ordenada
        i = ini - 1
        x = lista[fim]
    
        for j in range(ini , fim):
            comps += 1
            if lista[j] <= x:
                # Incrementa a posição do menor elemento
                i = i + 1
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        trocas += 1
        
        pivot = i + 1
  
        # Se há elementos à esquerda do pivô, coloca-os
        # no lado esquerdo da lista auxiliar
        if pivot - 1 > ini:
            pos = pos + 1
            aux[pos] = ini
            pos = pos + 1
            aux[pos] = pivot - 1
  
        # Se há elementos à direita do pivô, coloca-os
        # no lado direito da lista auxiliar
        if pivot + 1 < fim:
            pos = pos + 1
            aux[pos] = pivot + 1
            pos = pos + 1
            aux[pos] = fim

########################################################################

# # 10 MIL

# import tracemalloc
# from time import time
# import sys
# sys.dont_write_bytecode = True      # Impede a criação do cache

# from data.emp10mil import empresas

# comps = trocas = passadas = 0

# tracemalloc.start()		# Inicia a medição de memória
# hora_ini = time()
# quick_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) * 1000, 2)}ms")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

########################################################################

# # 25 MIL

# import tracemalloc
# from time import time
# import sys
# sys.dont_write_bytecode = True      # Impede a criação do cache

# from data.emp25mil import empresas

# comps = trocas = passadas = 0

# tracemalloc.start()		# Inicia a medição de memória
# hora_ini = time()
# quick_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) * 1000, 2)}ms")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

########################################################################

# # 50 MIL

# import tracemalloc
# from time import time
# import sys
# sys.dont_write_bytecode = True      # Impede a criação do cache

# from data.emp50mil import empresas

# comps = trocas = passadas = 0

# tracemalloc.start()		# Inicia a medição de memória
# hora_ini = time()
# quick_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) * 1000, 2)}ms")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

########################################################################

# 100 MIL

import tracemalloc
from time import time
import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from data.emp100mil import empresas

comps = trocas = passadas = 0

tracemalloc.start()		# Inicia a medição de memória
hora_ini = time()
quick_sort(empresas)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print("Nomes ordenados: ", empresas)
print(f"Tempo gasto: {round((hora_fim - hora_ini) * 1000, 2)}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")