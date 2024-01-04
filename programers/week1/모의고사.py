def solution(answers):
    
    answer = []
    
    a = [1, 2, 3, 4, 5]
    aScore = 0
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    bScore = 0
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cScore = 0
    
    for i in range(0, len(answers)):
        
        if len(answers) <= 5 :
            if answers[i] == a[i]:
                aScore = aScore + 1
            if answers[i] == b[i] :
                bScore = bScore + 1
            if answers[i] == c[i] :
                cScore = cScore + 1

        elif len(answers) <= 8 :
            if answers[i] == a[i % 5]:
                aScore = aScore + 1
            if answers[i] == b[i] :
                bScore = bScore + 1
            if answers[i] == c[i] :
                cScore = cScore + 1
                
        elif len(answers) <= 10 :
            if answers[i] == a[i % 5]:
                aScore = aScore + 1
            if answers[i] == b[i % 8] :
                bScore = bScore + 1
            if answers[i] == c[i] :
                cScore = cScore + 1
        
        else :
            if answers[i] == a[i % 5]:
                aScore = aScore + 1
            if answers[i] == b[i % 8] :
                bScore = bScore + 1
            if answers[i] == c[i % 10] :
                cScore = cScore + 1
        
    temp = [aScore, bScore, cScore]
    
    if max(temp) == aScore :
        answer.append(1)
    
    if max(temp) == bScore :
        answer.append(2)
    
    if max(temp) == cScore :
        answer.append(3)
    
    return answer