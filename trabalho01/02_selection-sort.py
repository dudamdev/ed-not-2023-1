"""
    ALGORITMO DE ORDENAÇÃO SELECTION SORT
"""
def selection_sort(lista):

    global comps, trocas, passadas
    comps = trocas = passadas = 0

    # Loop que vai da primeira até a PENÚLTIMA posição
    for pos_sel in range(len(lista) - 1):

        passadas += 1

        # Encontra o menor valor na sublista à frente de pos_sel
        pos_menor = pos_sel + 1
        for pos in range(pos_sel + 2, len(lista)):
            # Se o valor encontrado na posição for MENOR que o valor
            # da posição pos_menor, então pos_menor passa a ser pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # Compara os elementos das posições pos_menor e pos_sel. Se o valor
        # do primeiro for MENOR que o valor do segundo, efetua a troca
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

########################################################################################################################

# # 10 MIL

# import tracemalloc
# from time import time
# import sys
# sys.dont_write_bytecode = True      # Impede a criação do cache

# from data.emp10mil import empresas

# comps = trocas = passadas = 0

# tracemalloc.start()		# Inicia a medição de memória
# hora_ini = time()
# selection_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) / 60, 2)} minutos")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

##################################################################################

# 25 MIL

import tracemalloc
from time import time
import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from data.emp25mil import empresas

comps = trocas = passadas = 0

tracemalloc.start()		# Inicia a medição de memória
hora_ini = time()
selection_sort(empresas)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print("Nomes ordenados: ", empresas)
print(f"Tempo gasto: {round((hora_fim - hora_ini) / 60, 2)} minutos")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

##################################################################################

# # 50 MIL

# import tracemalloc
# from time import time
# import sys
# sys.dont_write_bytecode = True      # Impede a criação do cache

# from data.emp50mil import empresas

# comps = trocas = passadas = 0

# tracemalloc.start()		# Inicia a medição de memória
# hora_ini = time()
# selection_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) / 60, 2)} minutos")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")

##################################################################################

# # 100 MIL

# import tracemalloc
# from time import time
# import sys
# sys.dont_write_bytecode = True      # Impede a criação do cache

# from data.emp100mil import empresas

# comps = trocas = passadas = 0

# tracemalloc.start()		# Inicia a medição de memória
# hora_ini = time()
# selection_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) / 60, 2)} minutos")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passadas}")