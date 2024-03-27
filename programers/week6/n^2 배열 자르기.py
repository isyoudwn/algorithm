def solution(n, left, right):

    # status는 n의 묶음을 계산하기 위함
    status = 0
    answer = []
            
    # 10000000 이하로 해야하기 때문에 O(n)이하로 코드 작성
    # O(n) 코드에서 시간초과가 발생하여 최적화 하였음

    # n * n 배열을 잘라서 한줄로 만들었다고 가정하였음
    # 그 상태에서 left ~ right 까지의 값을 구해서 answer에 append 하여 반환 할 예정
    # n개 단위로 1차원 배열을 잘라서 묶음을 구하면 -> x번째 묶음은, 묶음 안에서의 인덱스 0 ~ x까지 (x + 1)로 해당 묶음이 채워진다.
    # ex) 0번째 묶음 : [1, 2, 3, 4] 1번째 묶음 : [2, 2, 3, 4]
    # 나머지 배열은 (묶음에서의 인덱스 + 1)이 채워진다. 
    for i in range(left, right + 1) :
        
        # index는, 현재 탐색 중인 i가 . . 묶음 안에서의 인덱스를 계산
        index = i % n
        # status는 현재의 묶음을 계산한다.
        status = i//n

        # 묶음 안에서의 0 ~ 묶음번 째 까지 (묶음 번 째 + 1)이 반복되어서 나오는 것을 표현
        if index >= 0 and index <= status :
            answer.append(status + 1)
        # 그 외의 것은 index + 1만큼 채워짐
        else :
            answer.append(index + 1)
    
    return answer