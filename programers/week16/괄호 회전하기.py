from collections import deque

def solution(s):
    answer = 0
    queue = deque(list(s))
    N = len(queue)
    

    for i in range(0, N):
        
        temp = queue
        stack = []
        
        for i in range(0, len(temp)):
            if (temp[i] == ']' or temp[i] == ')' or temp[i] == '}') and len(stack) == 0:
                break
                
            elif temp[i] == '[' or temp[i] == '{' or temp[i] == '(':
                stack.append(temp[i])

            elif stack[len(stack) - 1] == '[' and temp[i] == ']':
                stack.pop()
                
            elif stack[len(stack) - 1] == '{' and temp[i] == '}':
                stack.pop()
                
            elif stack[len(stack) - 1] == '(' and temp[i] == ')':
                stack.pop()
                
            else:
                break    
                

        else:
            if not stack:
                answer += 1
            
        queue.rotate(-1)

    return answer