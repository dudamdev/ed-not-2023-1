"""
    ESTRUTURA DE DADOS ÁRVORE BINÁRIA DE BUSCA
    * Árvore ~> é uma estrutura de dados não linear, considerada
    uma especialização do grafo, formada recursivamente por
    outras árvores (subárvores).
    * Árvore binária ~> uma árvore na qual cada nodo tem grau
    máximo igual a 2. Em outras palavras, cada nodo pode ter
    até dois descendêntes diretos.
    * Árvore binária de busca ~> é uma árvore binária em que as
    inserções são feitas de forma ordenada, de modo a otimizar a 
    operação de busca binária.
"""
class BinarySearchTree:

    """
        Classe que representa cada unidade de informação (nodo)
        da árvore binária de busca.
        Possui três artibutos:
        1) Informações relevantes para o usuário (data)
        2) Ponteiro para o nodo descendente à esquerda (left)
        3) Ponteiro para o nodo descendente à direita (right)
    """
    class Node: 
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None
    
    """
        Método construtor da classe BinarySearchTree
    """
    def __init__(self):
        self.__root = None      # Raiz da árvore
    
    """
        Método PÚBLICO para a inserção de um VALOR na árvore
    """
    def insert(self, val):
        # Cria um novo nodo para armazenar o valor
        new = self.Node(val)

        # 1° caso: a árvore está vazia.
        # O primeiro nodo inserido será a raiz
        if self.__root is None: self.__root = new

        # 2° caso: a raiz já existe. É necessário procurar pela
        # posição de inserção do novo nodo, o que é feito por
        # um método privado
        else: self.__insert_node(self.__root, new)

    """
        Método PRIVADO para inserção de um NODO na árvore
    """
    def __insert_node(self, root, new):
        # 1° caso: o valor do novo nodo é MENOR que o valor na raiz
        if new.data < root.data:
            # Se a esquerda da raiz estiver desocupada, insere aí
            if root.left is None: root.left = new
            # Senão, ássa a considerar o nodo da esquerda como raiz
            else: self.__insert_node(root.left, new)

        # 2° caso: o valor do novo nodo é MAIOR que o valor na raiz
        elif new.data > root.data:
            # Se a direita da raiz estiver desocupada, insere aí
            if root.right is None: root.right = new
            # Senão, passa a considerar o nodo da direita como raiz
            else: self.__insert_node(root.right, new)
