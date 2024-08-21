def solution(A,B):
    answer = 0

    a = sorted(A, reverse = True)
    b = sorted(B)
    
    a2 = sorted(A)
    b2 = sorted(B, reverse = True)

    sumAB = 0
    sumAB_2 = 0
    
    for i in range(0, len(a)):
        sumAB += a[i] * b[i]
        
    for i in range(0, len(a2)):
        sumAB_2 += a2[i] * b2[i]
    
    if sumAB > sumAB_2:
        answer = sumAB_2
    else:
        answer = sumAB

    return answer