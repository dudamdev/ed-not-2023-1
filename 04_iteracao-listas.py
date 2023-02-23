def linha():
    print("-" * 100, "\n")

# Lista
frutas = ["laranja", "maça", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer uma lista e exibir apenas os seus elementos,
# usamos for..in, como já vimos no arquivo 2
for f in frutas:
    print(f)

linha()

# Se quisermos percorrer a lista em ordem inversa para exibir apenas seus
# elementos, podemos usar for..in combinado com reversed()
for f in reversed(frutas):
    print(f)

linha()

# Agora precisamos exibir, além do elemento, também sua POSIÇÂO,
# devemos usar range()
for pos in range(len(frutas)):
    print(f"A fruta {frutas[pos]} está na posição {pos}.")

linha()

# Percurso em ordem inversa usando range() com 3 parâmetros
for i in range (len(frutas) -1, -1, -1): # len(frutas) - 1 = 6; -1 (para ir até o 0); -1 inverte o passo
    print(f"A fruta {frutas[i]} está na posição {i}.")



