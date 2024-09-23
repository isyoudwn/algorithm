def solution(elements):
    answer = 0
    window = len(elements)
    temp_arr = []
    result = set()
    elements = elements * 2
    elements.pop()
    
    start = 0
    end = window
    
    while start < window and end < len(elements) + 1:
        if start == 0 :
            
            for i in range(start, end):
                result.add(elements[i])
                temp_arr.append(elements[i])
            
        else:
            idx = 0
            
            for i in range(start, end):
                result.add(elements[i] + temp_arr[idx])
                temp_arr[idx] = elements[i] + temp_arr[idx]
                
                idx = idx + 1
        
        
        start = start + 1
        end = end + 1

        
    answer = len(result)
    
    return answer