def solution(s):
    answer = -1

    stack = []
    top = -1
    
    for value in s :
        if top == -1:
            stack.append(value)
            top += 1
            
        elif stack[top] == value:
            stack.pop()
            top -= 1
            continue
            
        else: 
            stack.append(value)
            top += 1
        
        
    if stack :
        answer = 0
    else:
        answer = 1

    return answer