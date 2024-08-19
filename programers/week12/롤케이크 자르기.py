from collections import Counter

def solution(topping):
    answer = 0
    N = len(topping)
    chulsoo = Counter(topping)
    brother = {}
    
    
    
    for i in range(0, N) :
        now = topping[i]
        
        if now not in brother:
            brother[now] = 1
            chulsoo[now] = chulsoo[now] - 1
               
        else:
            brother[now] = brother[now] + 1
            chulsoo[now] = chulsoo[now] - 1
            
        if brother[now] == 0:
            del brother[now]
        
        if chulsoo[now] == 0:
            del chulsoo[now]
            
        if len(brother) == len(chulsoo):
            answer = answer + 1
            
    
    return answer