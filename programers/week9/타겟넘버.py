answer = 0

def dfs(target, temp, arr, i, length) :
    
    global answer
    
    if temp == target and i == length:
        answer += 1 
        return
    
    elif i == length:
        return
    
    else:
        dfs(target, temp + arr[i], arr, i + 1, length)
        dfs(target, temp - arr[i], arr, i + 1, length)
        
    return
        
    
def solution(numbers, target):
    length = len(numbers)
    
    dfs(target, numbers[0], numbers, 1, length)
    dfs(target, -numbers[0], numbers, 1, length)

    
    return answer