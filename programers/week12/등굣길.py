def solution(m, n, puddles):
    answer = 0
    dp = []
    
    # n은 행 , m은 열
    
    for i in range(0, n):
        dp.append([])
        for j in range(0, m):
            dp[i].append(0)
            
    
    dp[0][0] = 1
    
    # i가 행 == n, j가 열 == m
    for i in range(0, n):
        for j in range(0, m):
            
            if i == 0 and j == 0:
                continue
            
            if [j + 1, i + 1] in puddles:
                dp[i][j] = 0
            
            #base case
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
                
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
            
    answer = dp[n - 1][m - 1] % 1000000007
    
    return answer