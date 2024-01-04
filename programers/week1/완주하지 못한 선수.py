# 완주하지 못한 선수
# 풀이 참조

def solution(participant, completion):

    participant.sort()
    completion.sort()
    
    for i in range(0, len(participant)) :
        
        if i == len(participant) - 1 :
            return participant[len(participant)-1]
        
        if participant[i] != completion[i] :
            return participant[i] 
        
        else :
            continue
    
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

result = solution(participant, completion)

print(result)