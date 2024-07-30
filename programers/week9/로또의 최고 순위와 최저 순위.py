def countMaxWin(lottos, win_nums) :
    
    if len(win_nums) >= lottos:
        return lottos
    else:
        return len(win_nums)
    
    
def formatting(num) :
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3 :
        return 4
    elif num == 2:
        return 5
    else :
        return 6
        

def solution(lottos, win_nums):
    answer = []
    defaultWin = 0
    minWin = 0
    maxWin = 0
    countZero = 0

    
    for l in lottos:
        if l == 0:
            countZero += 1
            continue
            
        if l in win_nums :
            win_nums.remove(l)
            defaultWin += 1
            
    if defaultWin == 6:
        return [1, 1]
    
    else :
        maxWin = defaultWin + countMaxWin(countZero, win_nums)
        minWin = defaultWin
        
        
        
    maxWin = formatting(maxWin)
    minWin = formatting(minWin)
    
    
    answer.extend([maxWin, minWin])
    

    return answer