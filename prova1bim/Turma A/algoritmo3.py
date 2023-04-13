"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

# 1) Algoritmo de ordenação BUBBLE SORT.

# 2) a: Define a função BUBBLE SORT.
#    b: Representa a lista (vetor) a ser ordenada.
#    c: Variável boleana que indica se houve troca na passada do loop "while"
#    d: Controla o índice de posição da lista.

# 3) Na primeira linha do "if" a variável boleana está sendo utilizada como índice de posição da lista "b[d + 1], b[c] = b[c], b[d + 1]". O correto seria substituí-la pela variável "d" que controla o índice de posição:
#   def a(b):
#       while True:
#           c = False
#           for d in range(len(b) - 1):
#               if b[d + 1] < b[d]:
#                   b[d + 1], b[d] = b[d], b[d + 1]
#                   c = True
#           if not c:
#              break

def a(b):
    while True:
        c = False
        for d in range(len(b) - 1):
            if b[d + 1] < b[d]:
                b[d + 1], b[c] = b[c], b[d + 1]
                c = True
        if not c:
            break