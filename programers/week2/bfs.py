def bfs(graph, start) :
    visited = []

    for node in graph:
        if node not in visited :
            visited.append(start)
        for n in graph[node] :
            if n not in visited :
                visited.append(n)
    
    return visited

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

result = bfs(graph, 'A')

print(result)