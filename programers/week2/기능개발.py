import math 

def solution(progresses, speeds):
    answer = []
    publish = []
    pivot = 0
    temp = 0
    
    # 배포일 list 생성
    # 배포는 일 단위이고, 소수점일 경우 다음날 배포해야 함 -> 올림 사용
    for i in range(len(progresses)) :
        publish.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    for i in range(len(publish)) :
        # 기준일을 정하고, 기준일의 배포 가능 날짜보다 배포 가능일이 빠를 경우 계산
        if publish[pivot] >= publish[i] :
            temp = temp + 1
            continue
        # 기준일의 배포 가능 날짜보다 배포 가능일이 늦을 경우, answer에 append하기
        # 기준일 변경
        else :
            answer.append(temp)
            temp = 1
            pivot = i 

    # 마지막 인덱스까지 탐색을 하게 된다면, 마지막 temp는 append가 안 됨 -> 추가적으로 append 해야지 마지막까지 탐색한 결과가 반영 됨.
    # ex) publish = [30, 5, 70, 90]
    # temp = 2 -> answer에 append() => else에서 temp = 1, pivot = 2로 초기화 => i = 3(마지막 인덱스) temp가 계산 된 후 append없이 for문 종료 => for문 밖에서 마지막 temp를 추가해줘야함          
    answer.append(temp)

    return answer