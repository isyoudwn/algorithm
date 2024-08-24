from collections import Counter

def solution(k, tangerine):
    answer = 0

    sorted_t = sorted(list(Counter(tangerine).values()), reverse = True)
    
    sum_value = 0
    
    for i in range(0, len(sorted_t)):
        sum_value = sorted_t[i] + sum_value
        
        if sum_value >= k:
            answer = i + 1
            break
            
    
    return answer