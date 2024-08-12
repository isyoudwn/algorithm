def solution(genres, plays):
    answer = []
    music = {}
    
    for idx, value in enumerate(genres):
        if value not in music:
            music[value] = [plays[idx], (idx, plays[idx])]
        else:
            music[value].append((idx, plays[idx]))
            music[value][0] += plays[idx]
            
    music = sorted(music.items(), key = lambda x:-(x[1][0]))

    temp = []
    temp_sorted = []
    for m in music:
        temp.append(m[1][1:])
        
    for t in temp:
        t = sorted(t, key=lambda x:(-x[1], x[0]))
        if len(t) < 2:
            temp_sorted.append(t[0:])
        else:
            temp_sorted.append(t[:2])
    
    
    for t in temp_sorted:
        for v in t:
            answer.append(v[0])
        
    
    return answer