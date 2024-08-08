from itertools import permutations

def solution(word):
    temp = []
    dic = []
    
    alpha = [
        'A', 'A', 'A', 'A', 'A', 
        'E', 'E', 'E', 'E', 'E',
        'I', 'I', 'I', 'I', 'I',
        'O', 'O', 'O', 'O', 'O', 
        'U', 'U', 'U', 'U', 'U'
    ] 
    
    for i in range(1, 6):
        temp.extend(list(set(permutations(alpha, i))))
    
    for i in temp:
        dic.append(''.join(i))
    
    dic.sort()
    
    return dic.index(word) + 1
    
