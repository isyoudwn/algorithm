def solution(sequence, k):
    answer = []
    N = len(sequence)
    
    end = 0
    sumValue = 0
    
    for start in range(0, N):
        
        if start == 0:
            sumValue = sequence[start]
        else:
            sumValue = sumValue - sequence[start - 1]
            
            
        if sumValue == k:
                if not answer:
                    answer.extend([start, end])
                    
                elif (answer[1] - answer[0]) > (end - start):
                    answer[0] = start
                    answer[1] = end
                    
        if sumValue > k:
            continue
        
        end = end + 1
        
        while (start < end) and (end < N):
            sumValue += sequence[end]
            
            if sumValue == k:
                if not answer:
                    answer.extend([start, end])
                    
                elif (answer[1] - answer[0]) > (end - start):
                    answer.extend([start, end])     
            
            elif sumValue > k:
                break
            
            end += 1
    
    return answer