# 최소직사각형

def solution(sizes):
    
    maxWidth = 0
    maxHeight = 0
    temp = 0
    answer = 0
    
    for i in range(0, len(sizes)):
        if sizes[i][0] < sizes[i][1] :
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
            
            
    for i in range(0, len(sizes)) :
        if maxWidth < sizes[i][0] :
            maxWidth = sizes[i][0]
            
        if maxHeight < sizes[i][1] :
            maxHeight = sizes[i][1]
    
    answer = maxWidth * maxHeight
            
    return answer