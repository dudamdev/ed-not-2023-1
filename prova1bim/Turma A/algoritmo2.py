"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

# 1) Algoritmo de BUSCA BINÁRIA.

# 2) a: Define a função BUSCA BINÁRIA.
#    b: Representa a lista (vetor) na qual será buscado o valor "c".
#    c: Valor a ser encontrado na lista "a".
#    d: Controla o índice da posição de inicio da lista.
#    e: Controla o índice da posição de fim da lista. 
#    f: Armazena a divisão inteira da soma entre o inicio e o fim da lista,
#       definindo sua metade.

# 3) O primeiro "if c == b[f]: e = f" deveria retornar "f" 
#    pois se o valor procurado "c" for igual ao valor do meio da lista "b[f]", 
#    significa que o valor foi encontrado. Logo, o correto seria:
#    def a(b, c):
#        d = 0
#        e = len(b) - 1
#        while d <= e: 
#            f = (d + e) // 2
#            if c == b[f]: return f
#            elif c < b[f]: e = f - 1
#            else: d = f + 1
#        return -1

def a(b, c):
    d = 0
    e = len(b) - 1
    while d <= e: 
        f = (d + e) // 2
        if c == b[f]: e = f
        elif c < b[f]: e = f - 1
        else: d = f + 1
    return -1