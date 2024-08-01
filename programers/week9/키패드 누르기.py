from collections import deque

def bfs(startNode, target, graph) :
    
    queue = deque([startNode])
    visited = set([startNode])
    distance = {startNode : 0}
    
    while(queue) :
        current = queue.popleft()
        
        if current == target : 
            return distance[current]
        
        for n in graph[current] :
            if n not in visited:
                visited.add(n)
                queue.append(n)
                
                distance[n] = distance[current] + 1
                
                
def solution(numbers, hand):
    answer = ''
    
    nowHand = {
        'L' : '*',
        'R' : '#'
    }
    
    graph = {
        1 : [2, 4],
        2 : [1, 3, 5],
        3 : [2,6],
        4 : [1,7,5],
        5 : [2,4,6,8],
        6 : [3,5,9],
        7 : [4,8, '*'],
        8 : [0,5,7,9],
        9 : [6, 8, '#'],
        0 : [8, '#', "*"],
        '*' : [0, 7],
        '#' : [0, 9]
    }
    
    for n in numbers :
        if n == 1 or n == 4 or n == 7:
            nowHand['L'] = n
            answer += 'L'
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            nowHand['R'] = n
        else :
            a = bfs(nowHand['L'], n, graph)
            b = bfs(nowHand['R'], n, graph)

            if a < b :
                answer += 'L'
                nowHand['L'] = n
            elif b < a:
                answer += 'R'
                nowHand['R'] = n
            else :
                if hand == "right":
                    answer += 'R'
                    nowHand['R'] = n
                else :
                    answer += 'L'
                    nowHand['L'] = n
    
    
    return answer