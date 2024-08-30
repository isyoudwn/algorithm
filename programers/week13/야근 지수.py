import heapq

def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    max_heap = []
    
    
    for w in works:
        heapq.heappush(max_heap, -w)
    
    for i in range(0, n):
        a = heapq.heappop(max_heap)
        a = a + 1
        heapq.heappush(max_heap, a)
        
    while max_heap:
        a = heapq.heappop(max_heap)
        if a >= 0:
            answer += 0
        else :
            a = (-a)**2
            answer += a
    
    return answer