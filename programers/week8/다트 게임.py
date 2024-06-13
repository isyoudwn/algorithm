def bonus_score(value, bonus) :
    if bonus == 'S':
        return value
    if bonus == 'D':
        return value * value
    if bonus == 'T':
        return value * value * value
    

def option_score(arr, option) :
    if option == '*':
        if len(arr) <= 1:
            arr[0] = arr[0] * 2
            return
        else :
            arr[len(arr) - 1] = arr[len(arr) - 1] * 2 
            arr[len(arr) - 2] = arr[len(arr) - 2] * 2 
            return
        
        
    if option == '#':
        if len(arr) <= 1:
            arr[0] = arr[0] * -1
        else :
            arr[- 1] = arr[- 1] * (-1)

        

def solution(dartResult):
    answer = 0
    score_arr = []
    i = 0
    
    while(i < len(dartResult)) :
        if dartResult[i].isdigit() and dartResult[i + 1].isdigit() :
            score_arr.append(10)
            i = i + 1
        
        elif i == 0 :
            score_arr.append(int(dartResult[i]))
    
        
        elif (dartResult[i].isdigit()) :
                score_arr.append(int(dartResult[i]))
        
        elif (dartResult[i].isalpha()):
            score_arr[- 1] = bonus_score(score_arr[- 1], dartResult[i])
            
        else :
            option_score(score_arr, dartResult[i])
            
        i = i + 1
        
        answer = sum(score_arr) 

    return answer