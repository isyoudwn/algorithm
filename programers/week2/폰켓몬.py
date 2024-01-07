from collections import Counter

#O(n)
def solution(nums):
    
    poketmon = Counter(nums)
    answer = 0
    limit = len(nums)/2
    
    print(poketmon)
    
    for k, v in poketmon.items() :
        answer = answer + 1
    
    if answer > limit:
        answer = limit
    
    return answer