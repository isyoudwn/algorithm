from collections import Counter
def solution(gems):
    answer = []
    
    N = len(gems)
    option_len = len(Counter(gems))
    
    check = {}
    
    start = 0
    end = 0
    
    if option_len <= 1 or N <= 1:
        return[1,1]
    
    
    for start in range(0, N):
        
        if start == 0:
            check[gems[start]] = 1
        
        else:
            check[gems[start - 1]] -= 1
            
            
            if check[gems[start - 1]] == 0:
                del check[gems[start - 1]]

                
        if option_len == len(check):
            if not answer:
                answer.extend([start, end])
            elif (answer[1] - answer[0]) > (end - start):
                answer[0] = start
                answer[1] = end
            elif (answer[1] - answer[0]) == (end - start):
                if answer[0] > start:
                    answer[0] = start
                    answer[1] = end

            continue
        end = end + 1
        while (start < end) and (end < N):
            if gems[end] not in check:
                check[gems[end]] = 1
                
            else:
                check[gems[end]] += 1
                
            if option_len == len(check):
                if not answer:
                    answer.extend([start, end])
                elif (answer[1] - answer[0]) > (end - start):
                    answer[0] = start
                    answer[1] = end
                    
                elif (answer[1] - answer[0]) == (end - start):
                    if answer[0] > start:
                        answer[0] = start
                        answer[1] = end
                    
                break
            
            end += 1

            
        
    answer = [answer[0] + 1, answer[1] + 1]
        
    
    return answer