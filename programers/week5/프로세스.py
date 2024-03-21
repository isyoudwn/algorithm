from collections import deque

# 1시간 30분 소요

def solution(priorities, location):
    # deque 정의
    deq = deque(priorities)
    # 내가 알고자 하는 process의 location
    target = location
    # 실행 된 process count
    process = 0

    # deq가 빌 때 까지 반복문 실행
    while(True) :
        # 만약 deq[0] 보다 중요한 프로세스가 있다면, status = 1
        status = 0
        
        # 탈출 조건
        if len(deq) == 0 :
            return process
    
        # deq[0] 보다 중요한 프로세스가 있는지 확인, 있으 경우 status = 1
        for i in range(1, len(deq)) :
            if deq[0] < deq[i] :
                status = 1
                break 
    
        # deq[0] 보다 중요한 프로세스가 있고, 내가 알고자 하는 프로세스가 deq[0]일 경우
        if status and target == 0 :
            # deq를 돌리고, target의 인덱스를 deq 끝으로 갱신
            deq.rotate(-1)
            target = len(deq) - 1
        # deq[0] 중요한 프로세스가 없고, 내가 알고자하는 프로세스가 deq[0]일 경우
        elif status == 0 and target == 0 :
            # process를 하나 더하고 return. -> 답 도출
            process = process + 1
            return process
        # deq[0]보다 중요한 프로세스가 있고, 내가 알고자 하는 프로세스가 deq[0]이 아닌 경우
        elif status :
            # deq를 돌리고, target이 앞으로 왔기 때문에 -1 해줌.
            deq.rotate(-1)
            target = target - 1
        # deq[0]보다 중요한 프로세스가 없고, 내가 알고자 하는 프로세스가 deq[0]이 아닌 경우  
        else :
            # deq[0]을 pop시킴
            deq.popleft()
            # target의 위치를 -1 해줌
            target = target - 1
            # process를 더함
            process = process + 1