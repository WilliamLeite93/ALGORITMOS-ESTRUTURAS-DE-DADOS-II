
mapa = {
    'Arad': [
        ('Zerind', 75),
        ('Sibiu', 140),
        ('Timisoara', 118)
        ],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
}

def busca_dfs(grafo, inicio, objetivo):
    pilha = [(inicio, [inicio], 0)]

    visitados = set()

    while pilha:
        no_atual, caminho, custo = pilha.pop()

        if no_atual == objetivo:
            return caminho, custo
        
        if no_atual not in visitados:
            visitados.add(no_atual)

            for vizinho, distancia in grafo[no_atual]:
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho], custo + distancia))
    
    return None, 0

caminho_dfs, custo_dfs = busca_dfs(mapa, 'Arad', 'Bucharest')
print("--- DFS ---")
print(f"caminho: {' -> '.join(caminho_dfs)}" if caminho_dfs else "Caminho não encontrado")
print(f"Custo total: {custo_dfs}")
