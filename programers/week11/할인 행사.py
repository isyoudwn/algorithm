from collections import Counter 

def solution(want, number, discount):
    answer = 0
    count = []
    want_dic = {}
    
    for idx, w in enumerate(want):
        want_dic[w] = number[idx]
    
    
    for idx, value in enumerate(discount):
        if len(discount) - idx < 10:
            break
        if want_dic == Counter(discount[idx:idx+10]):
            answer += 1
    
    return answer