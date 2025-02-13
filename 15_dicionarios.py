"""
    Dicionário é uma estrutura de dados fornecida pela linguagem
    Python, capaz de armazenar múltiplos valores em uma única
    variável, por meio de pares de chave-valor.
"""

# Um dicionário é delimitado por chaves {}
# Diferente das listas, que têm posições numeradas, os dicionários
# possuem posições NOMEADAS. Cada uma das posições nomeadas de um
# dicionário é chamada PROPRIEDADE.
pessoa = {
    "nome": "Orozimbo Oliveira Osório",
    "sexo": "M",
    "idade": 71,
    "peso": 76,
    "altura": 1.66,
    "aposentado": True,
    "filhos": ["Zeferina", "Asdrúbal", "Gercina"]
}

# Acessando os valores armazenados no dicionário
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Aposentado?", pessoa["aposentado"])

# Calculando o IMC (Índice de Massa Corporal) da pessoa
imc = pessoa["peso"] / pessoa["altura"] ** 2
print(f"O IMC de {pessoa['nome']} é {imc}.")

#################################################################

# Representando formas geométricas planas por meio de dicionários

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R"     # Retângulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T"     # Triângulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E"     # Elipse
}

# forma4 = {
#     "base": 11,
#     "altura": "batata",
#     "tipo": "T" 
# }

# forma4 = {
#     "fruta": 10,
#     "altura": "batata",
#     "tipo": "T" 
# }

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R":    # Retângulo
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":  # Triângulo
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E":  # Elipse
        return (forma["base"] / 2) * (forma["altura"] / 2) * pi
    else:
        return None
    
######################################################################

# Calculando a área das formas
print(f"Base: {forma1['base']}; altura: {forma1['altura']}; tipo: {forma1['tipo']}; ÁREA: {calcular_area(forma1)}")
print(f"Base: {forma2['base']}; altura: {forma2['altura']}; tipo: {forma2['tipo']}; ÁREA: {calcular_area(forma2)}")
print(f"Base: {forma3['base']}; altura: {forma3['altura']}; tipo: {forma3['tipo']}; ÁREA: {calcular_area(forma3)}")
# print(f"Base: {forma4['base']}; altura: {forma4['altura']}; tipo: {forma4['tipo']}; ÁREA: {calcular_area(forma4)}")