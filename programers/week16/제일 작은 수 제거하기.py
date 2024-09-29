def solution(arr):
    answer = []
    
    a = min(arr)
    arr.remove(a)
    
    answer = arr
    
    if answer:
        return answer
    else:
        return [-1]
