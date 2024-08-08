def solution(s):
    answer = ''
    temp = []
    
    temp.extend(map(int, s.split(' ')))
    
    maxValue = str(max(temp))
    minValue = str(min(temp))
    
    answer = minValue + " " + maxValue
    
    return answer