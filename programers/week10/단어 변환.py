visited = []
answer = 52
N = 0

def compare(string1, words) :
    global visited
    arr = []
    stringArr = list(string1)
    
    for w in words:
        if w == string1:
            continue
            
        temp = 0

        if visited[words.index(w)] == 1:
            continue
            
        for i in range(0, len(stringArr)):
                if w[i] == stringArr[i] :
                    continue
                else :
                    temp = temp + 1
                    
        if temp <= 1 :    
            arr.append(w)
        
    return arr
    
    

def backTrack(now, target, temp, words) :
    
    global visited, answer
    
    if temp >= answer:
        return
    
    if now == target:
        answer = temp
        return
    
    for w in compare(now, words):
        print(w)
        visited[words.index(w)] = 1
        backTrack(w, target, temp + 1, words)
        visited[words.index(w)] = 0
    
    return
        

def solution(begin, target, words):

    global visited, answer, N
    
    N = len(words)
    
    visited = [0] * N
    
    backTrack(begin, target, 0, words)
    
    if answer == 52:
        return 0
    

    
    return answer