from itertools import permutations
    
def solution(k, dungeons):
    answer = -1
    maxValue = 0
    
    
    n = len(dungeons)
    p = list(permutations(dungeons, n))
    
    for i in p:
        temp = 0
        k_temp = k
        
        for j in i :
            if k_temp >= j[0] :
                temp += 1
                k_temp -= j[1]
            else :
                continue
                
        if maxValue <= temp:
            maxValue = temp
            
    answer = maxValue
            
    
    return answer