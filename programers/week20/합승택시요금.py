from collections import defaultdict
import heapq

def dijks(graph, start) :
    costs = defaultdict(int)
    queue = []
    
    heapq.heappush(queue, (0, start))
    
    while queue:
        
        now_cost, now_node = heapq.heappop(queue)

        if now_node in costs:
            continue
            
        costs[now_node] = now_cost
        
        for next_node, next_cost in graph[now_node]:
            heapq.heappush(queue, (next_cost + now_cost, next_node))
    
    return costs
            
            
            

def formatting(fares) :
    graph = defaultdict(list)
    
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
    return graph

def solution(n, s, a, b, fares):
    answer = 0
    graph = formatting(fares)
    result_table = []
    
    # start에서 n, n에서 a와 b까지 최소거리
    n_costs = dijks(graph, s)
    
    for node, cost in n_costs.items():
        costs = dijks(graph, node)
        
        if a not in costs or b not in costs:
            continue
            
        result_table.append((cost, costs[a], costs[b]))

    a = list(map(sum, result_table))
    
    answer = min(a)
    
    return answer