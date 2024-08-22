# def solution(triangle):
#     answer = 0
#     N = len(triangle[len(triangle) - 1])
#     dp = []
    
#     for i in range(0, N):
#         dp.append([])
#         for j in range(0, len(triangle[i])):
#             dp[i].append(-1)
            
#     # base-case
#     dp[0][0] = triangle[0][0]

    
#     for i in range(1, N):
#         for j in range(0, i + 1):
#             if j == 0:
#                 dp[i][j] = dp[i - 1][j] + triangle[i][j]
                
#             elif j == i:
#                 dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                
#             else:
#                 dp[i][j] = max(dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j])
                
#     answer = max(dp[N - 1])

    
#     return answer


def solution(triangle):
    answer = 0
    N = len(triangle[len(triangle) - 1])
    dp = triangle.copy()
            
    # base-case
    dp[0][0] = triangle[0][0]

    
    for i in range(1, N):
        for j in range(0, i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
                
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                
            else:
                dp[i][j] = max(dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j])
                
    answer = max(dp[N - 1])

    
    return answer