from collections import defaultdict

def solution(n, words):
    answer = []
    before = defaultdict(int)
    N = len(words)
    
    for i in range(0, N):
        if i == 0:
            before[words[i]] = 0
            
        elif len(words[i]) == 1 or words[i-1][-1] != words[i][0] or words[i] in before:
            # 사람
            person = i % n + 1
            # 번째
            person_num = i // n + 1
            answer = [person, person_num]
            break
        else:
            before[words[i]] = 0
    else:
        answer = [0, 0]
            


    return answer