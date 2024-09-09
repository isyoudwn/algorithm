from collections import defaultdict

def solution(n):
    answer = 0
    
    dp = defaultdict(int)
    
    for i in range(0, n + 1):
        dp[i]
    
    #base-case
    dp[1] = 1
    dp[2] = 1
    
    for i in range(1, n + 1):
        
        if (i - 1) in dp:
            if dp[i-1] != 0:
                dp[i] += dp[i - 1] 
            
        if (i - 2) in dp:
            if dp[i-2] != 0:
                dp[i] += dp[i - 2]
            
    answer = dp[n]%1234567

        
    
    return answer