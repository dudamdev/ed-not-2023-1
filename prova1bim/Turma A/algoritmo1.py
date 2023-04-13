"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

# 1) Algoritmo de ordenação MERGE SORT.

# 2) a: Define a função MERGE SORT.
#    b: Representa a lista (vetor) a ser ordenada.
#    c: Encontra a posição do meio da lista, para fazer a divisão em duas metades.
#    d: Armazena uma cópia da primeira metade da lista (sub-lista) e depois
#       chama recursivamente a função para que ela continue repartindo a sub-lista 
#       em duas partes menores.
#    e: Armazena uma cópia da segunda metade da lista (sub-lista) e depois
#       chama recursivamente a função para que ela continue repartindo a sub-lista 
#       em duas partes menores.
#    f: Controla o índice da posição da sub-lista gerada em "d".
#    g: Controla o índice da posição da sub-lista gerada em "e".
#    h: Armazena a sobra dos elementos restantes das sub-listas "d" e "e".
#    i: Armazena os elementos ordenados da sub-lista "d" e "e".

# 3) A lista "i" está sendo usada para armazenar os elementos ordenados da sub-lista "d" e "e",
#    mas também para armazenar a sobra dos elementos restantes das sub-listas. Nesse caso,
#    o correto seria substituir a variável "i" pela "h" no segundo "if". Dessa forma:
#    def a(b):
#        if len(b) <= 1: return b
#        c = len(b) // 2
#        d = b[:c]
#        e = b[c:]
#        d = a(d)
#        e = a(e)
#        f = g = 0
#        h = []
#        i = []
#        while f < len(d) and g < len(e):
#            if d[f] < e[g]:
#                i.append(d[f])
#                f += 1
#            else:
#                i.append(e[g])
#                g += 1
#        if(f < g): h = d[f:]
#        else: h = e[g:]
#        return h + i

def a(b):
    if len(b) <= 1: return b
    c = len(b) // 2
    d = b[:c]
    e = b[c:]
    d = a(d)
    e = a(e)
    f = g = 0
    h = []
    i = []
    while f < len(d) and g < len(e):
        if d[f] < e[g]:
            i.append(d[f])
            f += 1
        else:
            i.append(e[g])
            g += 1
    if(f < g): i = d[f:]
    else: i = e[g:]
    return h + i