def solution(n):
    answer = 0

    ans = list(str(n))
    ans = list(map(int, ans))
    
    answer = sum(ans)
    
    return answer