def solution(A, B):
    answer = 0
    N = len(A)
    
    i = 0
    j = 0
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    while i < N :
        
        if A[i] >= B[j]:
            i = i + 1
            
        else :
            i = i + 1
            j = j + 1
            
            answer += 1


    return answer