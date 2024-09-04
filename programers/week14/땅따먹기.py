def solution(land):
    answer = 0
    N = len(land)
    #base-case:
    memo = land.copy()

    for i in range(1, N):
        memo[i][0] += max(memo[i - 1][1], memo[i - 1][2], memo[i - 1][3])
        memo[i][1] += max(memo[i - 1][0], memo[i - 1][2], memo[i - 1][3])
        memo[i][2] += max(memo[i - 1][0], memo[i - 1][1], memo[i - 1][3])
        memo[i][3] += max(memo[i - 1][0], memo[i - 1][1], memo[i - 1][2])
        
    answer = max(memo[N - 1])
    

    return answer