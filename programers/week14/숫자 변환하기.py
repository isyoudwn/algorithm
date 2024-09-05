from collections import defaultdict

def solution(x, y, n):
    answer = 0
    dp = defaultdict(int)
    
    #base-case
    dp[x*2] = 1
    dp[x*3] = 1
    dp[x+n] = 1

    if x == y:
        return 0
    
    for i in range(x + 1, y + 1):
        temp = []
        
        if i/2 in dp:
            temp.append(dp[i/2] + 1)          
        if i/3 in dp:
            temp.append(dp[i/3] + 1)
        if i-n in dp:
            temp.append(dp[i-n] + 1)
        
        if temp :
            minValue = min(temp)
            if i in dp :
                if dp[i] > minValue:
                    dp[i] = minValue
            else:
                dp[i] = minValue

                
    if y in dp:
        answer = dp[y]
    else:
        answer = -1
        
        
    return answer