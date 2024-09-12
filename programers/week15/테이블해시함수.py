def solution(data, col, row_begin, row_end):
    answer = 0
    temp = [] 
    
    # col번쨰 컬럼의값으 기준으로 오름차순
    # 값이 동일하면 첫번째 컬럼 기준으로 내림차순
    
    # 정렬되면 1 - n 번째로 행 나누면... 거기의 행을 기준으로 애들 더하기 -> 나머지들 다 더하기
    # row_begin ~ row_end (행) 누적함
    
    # 100000 -> nlogn
    
    data = sorted(data, key=lambda x:(x[col - 1], -x[0]))
    
    for i in range(0, len(data)):
        t = sum(map(lambda x : x%(i + 1), data[i]))
        temp.append(t)

    answer = temp[row_begin-1]

    for i in range(row_begin, row_end):
        answer = answer ^ temp[i]

    return answer 