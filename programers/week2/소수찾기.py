from itertools import permutations

def solution(numbers):
    answer = 0
    tempList = []
    totalList = []
    result = []
    
    # 순열로 뽑아서 모든 경우의 수 list에 넣기
    for i in range(1, len(numbers) + 1) :
        tempList.append(list(permutations(list(numbers), i)))
    
    # 튜플 list로 만들기
    for i in range(0, len(tempList)) : 
        for j in range(0, len(tempList[i])) :
                totalList.append(list(tempList[i][j]))   

    # 앞자리 0인 거 0빼고 나머지로 만들기
    for i in range(0, len(totalList)) :
        if len(totalList[i]) < 2:
            continue

        for j in range (0, len(totalList[i])):
            if totalList[i][j] != '0':
                totalList[i] = totalList[i][j:]
                break
            if j == len(totalList[i])-1:
                totalList[i] = '0'

    
    # 중복 제거
    for i in range(0, len(totalList)) :
        result.append(''.join(totalList[i]))

    result = list(set(result))
    
    print(result)
    
    # 소수인지 계산
    for i in range(0, len(result)) :
        
        if result[i] == '0' :
            continue
            
        if result[i] == '1' :
            continue
        
        answer = answer + 1
    
        for j in range(2, int(result[i])) :
            if int(result[i]) % j == 0:
                answer = answer - 1
                break

    return answer
