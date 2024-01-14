
# O(n^2)
def solution(citations):
    answer = 0
    hIndex = []
    n = len(citations)
    
    # 인용 횟수 기준 for문 돌림
    # hIndex는 n 이하이기 때문에, n 이하 수 중 가장 큰 n 구하면 그것이 hIndex가 된다.
    # 따라서 range를 0 ~ n까지로 지정
    for h in range(0, n + 1) :
        hIndexValue = 0
        # citations 배열을 탐색하면서, h번 이상 인용된 논문 계산
        for j in range(0, n) :
            # 만약 citations[j]가  h번 이상 인용된 논문이라면 
            if h <= citations[j] :
                # 해당하는 것을 계산
                hIndexValue = hIndexValue + 1
                
                
        #  citations[j]가(인용 횟수가)  h번 이상인 것이 h편 이상이면서, 나머지 인용 안 된 것이 h번 이하이면, hIndex에 추가
        if hIndexValue >= h and n - hIndexValue <= h :
            # hIndex를 모아두는 배열에 append
            hIndex.append(h)
            
        # hIndex의 값들 중 가장 큰 것을 구해서 answer로 반환 
        answer = max(hIndex)

    return answer