"""
    Classe é uma estrutura que representa conjuntamente dados e algoritmos.
    Uma classe pode ser comparada a uma "assadeira" com a qual se pode
    produzir diferentes "assados" (objetos), variando os "ingredientes"
    (dados) e o "modo de fazer" (algoritmo). Apesar dessa variação, todos
    os objetos criados a partir de uma classe terão sempre o formato 
    determinado por esta. 
"""
"""
    PascalCase ---- FormaGeometrica ---- nome de classe na maioria das linguagens
    camelCase  ---- getElementById  ---- variáveis e nomes de funções em JavaScript e Java
    snake_case ---- memory_peak     ---- variáveis e nomes de funções em Python e C
    slug-case  ---- font-family     ---- propriedades em CSS
"""

# Por convenção, nomes de classes seguem a convenção PascalCase
class FormaGeometrica:
    """
        Uma classe pode ter, dentro de si, tanto dados quanto funções
        (estas, representando os algorítmos). Uma função especial,
        chamada __init__, é chamada smepre que um novo objeto é criado
        a partir de uma classe. Essa função especial é chamada de
        CONSTRUTOR.

        Quando aparecem dentro de uma classe:
         ~> funções passam a ser chamadas de MÉTODOS, e seu primeiro
         parâmetro é sempre self, que representa o próprio objeto
         ~> variáveis passam a ser chamadas ATRIBUTOS
    """
    def __init__(self, base, altura, tipo):

        # Validação dos parâmetros recebidos
        if type(base) not in [int, float] or base <= 0:
            raise Exception(f"ERRO: a base ({base}) deve ser numérica e maior que zero.")
        
        if type(altura) not in [int, float] or altura <= 0:
            raise Exception(f"ERRO: a altura ({altura}) deve ser numérica e maior que zero.")
        
        if tipo not in ["R", "T", "E"]:
            raise Exception(f"ERRO: o tipo ('{tipo}') deve ser 'R', 'T' ou 'E'.")

        # Armazenando os dados recebidos DENTRO do objeto, com self
        self.__base = base
        self.__altura = altura
        self.__tipo = tipo

##############################################################################################

# Criando um objeto chamado formal a partir da classe FormaGeometrica
forma1 = FormaGeometrica(10, 7.2, "T")

forma1.base = "batata"
forma1.altura = -4

print(f"Base: {forma1.base}")
print(f"Altura: {forma1.altura}")
print(f"Tipo: {forma1.__tipo}")