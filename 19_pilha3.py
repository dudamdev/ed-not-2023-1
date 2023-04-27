from lib.stack import Stack

# expr = "2 + (( 5 * ( 3 / 2 + 1) / 4 ))" expressão com a quantidade certa de parênteses
# expr = "(2 + (( 5 * ( 3 / (2 + 1) / 4 ))" expressão com mais parênteses abertos do que fechados
expr = "2 + (( 5 * ( 3 / 2 ) + 1)) / 4 ))" # expressão com mais parênteses fechados do que abertos


print(f"EXPRESSÃO ANALISADA: {expr}")

pilha = Stack()

# Percorre a expresão em busca de parênteses
for pos in range(len(expr)):
    # Empilha a posição quando é encontrado um abre parênteses
    if expr[pos] == "(":
        pilha.push(pos)
        # print(pilha)
    
    # Desempilha a posição do último abre parêntese empilhado
    # quando um fecha parênteses é encontrado
    elif expr[pos] == ")":
        if pilha.is_empty():
            print(f"Parênteses fechado na posição {pos} sem aberto correspondente")
        else:
            pos_abre = pilha.pop()
            print(f'Parêntese aberto na posição {pos_abre} foi fechado na posição {pos}')
            print(pilha)

# Verifica sobras na pilha
while not pilha.is_empty():
    pos_abre = pilha.pop()
    print(f"ERRO: parêntese aberto na posição {pos_abre} não possui o fechamento correspondente")

