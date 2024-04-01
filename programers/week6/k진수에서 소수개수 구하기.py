def solution(n, k):
    answer = 0
    number = []
    strr = ""

    # k진수 변환
    while(n > 0) :
        strr = strr + str(n % k)
        n = n // k

    # step이 양수일 때: 오른쪽으로 step만큼 이동 (정방향)
    # step이 음수일 때: 왼쪽으로 step만큼 이동 (역방향)
    # 0을 기준으로 자른다.
    number = strr[::-1].split('0')
    
    # 소수 구하기
    for item in number :
        if item == "" :
            continue
        else :
            it = int(item)
            if it == 1 :
                continue
            isPrime = True
            # 2부터 ~ 제곱근 이하의 수 까지 나누어 떨어지는 것이 있으면 소수가 아니다.
            for j in range(2, int(it**0.5)+1) :
                if it % j == 0 :
                    isPrime = False
                    break
            if isPrime :
                answer = answer + 1
        
    return answer