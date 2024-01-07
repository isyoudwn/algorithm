def solution(n, lost, reserve):

    # 정렬 : 정렬이 안 된 test-case도 존재하기 때문
    reserve.sort()
    lost.sort()
    
    # reserve의 요소 중 lost에 포함 된다면 제거하여 list 생성
    _reserve = [r for r in reserve if r not in lost]

    # lost의 요소 중 reserve에 포함 된다면 제거하여 list 생성
    _lost = [l for l in lost if l not in reserve]

    # 여분의 체육복을 가지고 있던 학생이 도난 당하였을 경우 본인이 입어야 하기 때문.

    # _reserve 탐색
    for r in _reserve:
        front = r - 1
        behind = r + 1

        # r의 front 값이 _lost에 존재하면, _lost에서 삭제
        if front in _lost:
            _lost.remove(front)
        # r의 behind 값이 _lost에 존재하면, _lost에서 삭제
        elif behind in _lost:
            _lost.remove(behind)

    # lost에는 못 빌린 사람만 남음.
            
    return n - len(_lost)