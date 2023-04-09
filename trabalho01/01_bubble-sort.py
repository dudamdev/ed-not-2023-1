"""
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
"""
# Variáveis de estatística
comps = trocas = passadas = 0

def bubble_sort(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0

    # Loop eterno, não sabemos quantas passadas serão necessárias
    while True:
        trocou = False
        passadas += 1

        # Percurso da lista, do primeiro ao PENÚLTIMO
        # elemento, com acesso a cada posição
        for pos in range(len(lista) -1):
            comps += 1
            
            # Se o número que está à frente na lista
            # for MENOR do que o que está atrás, TROCA        
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True
                trocas += 1
        
        if not trocou:  # não houve troca na passada
            break       # Interrompe o loop eterno; acabou

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
# bubble_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) / 1000 / 60, 2)} minutos")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, Trocas: {trocas}, Passadas: {passadas}")

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
# bubble_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) / 1000 / 60, 2)} minutos")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, Trocas: {trocas}, Passadas: {passadas}")

##################################################################################

# # 25 MIL

# import tracemalloc
# from time import time
# import sys
# sys.dont_write_bytecode = True      # Impede a criação do cache

# from data.emp25mil import empresas

# comps = trocas = passadas = 0

# tracemalloc.start()		# Inicia a medição de memória
# hora_ini = time()
# bubble_sort(empresas)
# hora_fim = time()

# # Captura as informações de gasto de memória
# mem_atual, mem_pico = tracemalloc.get_traced_memory()

# print("Nomes ordenados: ", empresas)
# print(f"Tempo gasto: {round((hora_fim - hora_ini) / 1000 / 60, 2)} minutos")
# print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
# print(f"Comparações: {comps}, Trocas: {trocas}, Passadas: {passadas}")

##################################################################################

# 10 MIL

import tracemalloc
from time import time
import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from data.emp10mil import empresas

comps = trocas = passadas = 0

tracemalloc.start()		# Inicia a medição de memória
hora_ini = time()
bubble_sort(empresas)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

print("Nomes ordenados: ", empresas)
print(f"Tempo gasto: {round((hora_fim - hora_ini) / 1000 / 60, 2)} minutos")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Comparações: {comps}, Trocas: {trocas}, Passadas: {passadas}")