def solution(msg):
    answer = []
    word = ""
    
    dic = {}
    number = 1
    
    # 딕셔너리 초기화
    for i in range(65, 91):
        dic[chr(i)] = number
        number = number + 1

    i = 0
    while (i < len(msg)):
        word = msg[i]
        
        if i == len(msg) - 1:
            if word in dic:
                answer.append(dic[word])
        
        for j in range(i + 1, len(msg)):
            
            temp = word + msg[j]
            
            if j == len(msg) - 1:
                if temp in dic:
                    answer.append(dic[temp])
                
            if temp in dic :
                word = temp
                i = j
            else :
                answer.append(dic[word])
                #사전에 등록
                dic[temp] = list(dic.values())[-1] + 1
                break
        #인덱스 증가
        i = i + 1
    
            
    
    return answer