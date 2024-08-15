def solution(s):
    answer = ''
    
    s = s.lower()
    temp = s.split(' ')
    

    for idx, t in enumerate(temp):
        string = ''
        if t == '':
            answer += ''
            
        elif t.isalpha():
            string = t[0].upper()
        else:
            string = t[0]
            
            
        for i, value in enumerate(t):
            if i == 0:
                continue
            string += value
        
        if idx == len(temp) - 1:
            answer += string
        else:
            answer += string + ' '
    
    
    return answer