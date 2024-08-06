def solution(brown, yellow):
    answer = []
    temp = []
    
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            j = yellow / i
            temp.append((j, i))

        
    
    for t in temp :
        if (t[0] * 2) + (t[1] * 2) + 4 == brown:
            return (t[0] + 2, t[1] + 2)
                    
        
    
    return answer