from collections import deque

def solution(people, limit):
    answer = 0
    # 한 번에 2명
    # 무게 제한
    # 구명보트 개수 최솟값
    # 즉 한번 보낼때 최대한 무게를 채워서 보내야함.
    people.sort()
    end = len(people) - 1
    start = 0
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start = start + 1
            
        end = end - 1
        answer = answer + 1 
        
    return answer