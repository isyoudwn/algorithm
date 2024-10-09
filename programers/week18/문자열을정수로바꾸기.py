def solution(s):
    answer = 0
    

    if s[0] == '+':
        answer = int(s[1:])
        
    elif s[0] == '-':
        answer = -int(s[1:])
        
    else:
        return int(s)
            
        
    return answer