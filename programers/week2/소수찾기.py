from itertools import permutations

def solution(numbers):
    answer = 0
    tempList = []
    result = []
    
    # 순열로 뽑아서 모든 경우의 수 list에 넣기
    for i in range(1, len(numbers) + 1) :
        tempList.append(set(permutations(list(numbers), i)))

        
    for i in range(0, len(tempList)) :
        for j in tempList[i]:
            result.append(''.join(j))

            
    result = list(set(map(int, result)))

    # 소수인지 계산
    for i in range(0, len(result)) :
        
        if result[i] == 0 :
            continue
            
        if result[i] == 1 :
            continue
        
        answer = answer + 1
    
        for j in range(2, int(result[i])) :
            if int(result[i]) % j == 0:
                answer = answer - 1
                break

    return answer

