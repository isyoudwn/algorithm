def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees:
        arr = []
        temp = []
        for sk in skill:
            try:
                arr.append(s.index(sk))
            except:
                arr.append(1000)
                
        temp = sorted(arr)

        if temp == arr:
            answer += 1
        
    return answer