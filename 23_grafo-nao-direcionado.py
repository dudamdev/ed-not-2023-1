from lib.graph import Graph

estradas = Graph()
print(estradas)

estradas.add_vertex("Fraca")
print(estradas)
print(f"Grau Franca: {estradas.degree('Franca')}")

estradas.add_edge("Franca", "Batatais", "Rod. Candido Portinari")
print(estradas)
print(f"Grau Franca: {estradas.degree('Franca')}")


estradas.add_edge("Franca", "Restinga")
print(estradas)
print(f"Grau Franca: {estradas.degree('Franca')}")

# Remoção da aresta Batatais <-> Franca
estradas.remove_edge("Batatais", "Franca", "Rod. Candido Portinari")
print(estradas)

# Tentativa de apagar o vértice "Batatais"
estradas.remove_vertex("Batatais")
print(estradas)
