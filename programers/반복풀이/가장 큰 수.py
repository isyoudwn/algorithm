def solution(number, k):
    answer = ''
    stack = []
    
    for n in number:
        if len(stack) == 0:
            stack.append(n)
            continue
        
        while k > 0 and len(stack) > 0 and stack[- 1] < n :
            stack.pop()
            k -= 1       
        stack.append(n)
        
    if k != 0:
        while k != 0:
            stack.pop()
            k -= 1
    answer = ''.join(stack)
    
    return answer