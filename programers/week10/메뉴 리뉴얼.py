from itertools import combinations

def solution(orders, course):
    answer = []
    
    dic = {}
    temp_dic = {}
    
    for key, value in enumerate(orders):
        dic[key] = []
        
        for c in course:
            dic[key].extend(list(combinations(value, c)))
        
    for key, value in dic.items():
        for i in value:
            a = list(i)
            a.sort()
            
            order = ''.join(a)
            if order not in temp_dic:
                temp_dic[order] = [[key + 1], 1]
            else:
                temp_dic[order][0].append(key + 1)
                temp_dic[order][1] += 1
        

    indexArr = []
    for c in course:
        maxValue = 0
        for key, value in temp_dic.items():
            if len(key) == c and value[1] >= 2:
                if value[1] > maxValue:
                    maxValue = value[1]
        if maxValue != 0:
            for key, value in temp_dic.items():
                if len(key) == c and value[1] == maxValue:
                    answer.append(key)
    answer.sort()

    
    return answer