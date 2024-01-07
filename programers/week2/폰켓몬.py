from collections import Counter

#O(n)
def solution(nums):
    
    poketmon = Counter(nums)
    answer = 0
    limit = len(nums)/2
    answer = len(poketmon)
    
    # len가 n/2를 넘을 경우
    if answer > limit:
        answer = limit
    
    return answer