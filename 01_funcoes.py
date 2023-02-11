# def --> define uma função
"""
    Função para calcular o Índice de Massa Corpórea (IMC)
    de uma pessoa, dados o seu peso e sua altura
"""
def imc(peso, altura):
    # peso dividido pela altura elevada ao quadrado
    return peso / altura ** 2

# resultado = variável --> no Python não é necessário declarar a variável
resultado = imc(81, 1.72)
print ('O IMC calculado é ', resultado)

##########################################################################

from math import pi # importa biblioteca matemática do Python

def calcular_area(base, altura, tipo):
    if tipo == "R":     # Retângulo
        return base * altura
    elif tipo == "T":   # Triângulo
        return base * altura / 2
    elif tipo == "E":   # Elipse ou círculo
        return (base / 2) * (altura / 2) * pi
    else:
        return None