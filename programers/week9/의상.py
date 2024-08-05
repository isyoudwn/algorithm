from itertools import combinations

def solution(clothes):
    answer = 1
    dic = {}
    
    for c in clothes:
        dic[c[1]] = []
    
    for c in clothes:
        dic[c[1]].append(c[0]) 
        
    
    
    for key, value in dic.items():
        answer = answer * (len(list(combinations(value, 1))) + 1)
    
    answer = answer - 1
    
    
    return answer