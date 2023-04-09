"""
    ALOGRITMO DE ORDENAÇÃO QUICK SORT RECURSIVO
"""
# Variáveis de estatística
passadas = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):

    # Quando não soubermos o valor da variável "fim",
    # vamos atribuir a ela a última posição da lista
    if fim is None: fim = len(lista) -1

    # Para que o algoritmo trabalhe, é necessário que a faixa delimitada
    # pelas variáveis "ini" e "fim" tenha, pelo menos, dois elementos.
    # Caso contrário, saímos da função sem fazer nada
    if fim <= ini: return

    global passadas, comps, trocas

    # Inicialização das variávies
    pivot = fim
    div = ini - 1
    passadas += 1

    # Percorre a lista da posição "ini" até a posição "fim" -1
    for pos in range(ini, fim):
        # Compara os elementos das posições "pos" e "pivot"
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1
            # Se os valores das variáveis "div" e "pos" forem diferentes
            # entre si e o elemento da posição "pos" for menor que o elemento
            # da posição "div", promove a troca entre eles
            comps += 1
            if pos != div and lista[pos] < lista[div]:
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    # Depois que o loop acaba, o divisor é implementado ainda uma vez
    div += 1

    # Caso os valores das posições "div" e "pivot" sejam diferentes entre si,
    # é feita a comparação entre os elementos dessas posições. Se o valor de
    # "pivot" for menor, promove-se a troca entre os elementos.
    comps += 1
    if pivot != div and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    # O ELEMENTO DA POSIÇÃO "div" ESTÁ EM SEU LUGAR CORRETO AGORA.

    # Chamamos recusivamente a função para ordenar a sublista à esquerda
    # da posição "div"
    quick_sort(lista, ini, div -1)

    # Fazemos o mesmo para ordenar a sublista à direita de "div"
    quick_sort(lista, div + 1, fim)

####################################################################################

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

####################################################################################

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

####################################################################################

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

####################################################################################

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


