from collections import Counter

def solution(N, stages):
    answer = []
    players = 0
    not_clear = 0
    dic1 = {}
    sum_a = 0
    sum_b = 0
    dic2 = {}
    
    
    dic1 = Counter(stages)  
        
    sorted_dic1 = dict(sorted(dic1.items()))
    
    sum_a = sum(sorted_dic1.values())
    
    for i in range(1, N + 1) :
        players = 0
        not_clear = 0
        
        if i in sorted_dic1 :
            not_clear = sorted_dic1[i]
            players = sum_a - sum_b
            dic2[i] = not_clear / players
            sum_b += sorted_dic1[i]
        else :
            dic2[i] = 0
    
    sorted_dic2 = sorted(dic2.items(), key = lambda item:item[1], reverse=True)
    
    
    for i in range (0, len(sorted_dic2)) :
        answer.append(sorted_dic2[i][0])
    
    return answer