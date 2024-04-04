def solution(n, t, m, p):
    answer = ''

    # 숫자를 한자리씩 잘라서 넣을 배열
    temp = []

    # n : 진법
    # t : 미리 구할 숫자의 개수
    # m : 게임에 참가하는 인원
    # p : 튜브의 순서
    
    # 2진수 ~ 16진수 구하기
    # 시간복잡도가 제한이 없기 때문에 최대 범위로 지정 -> while(True)로 변경해도 괜찮을 거 같음
    # i의 범위를 0 ~ t * m + 1로 하였음 
    # (why?) 우리는 한자리씩 잘라서 말할 것임 -> 내가 말해야하는 개수는 t개이다. -> m이라는 묶음 단위로 반복할 것이며, 나는 이 묶음이 t번 반복되기 전에 숫자를 다 말할것이다.

    # [main logic]
    # n진수로 변환하여 temp 배열에 한자리 씩 잘라서 넣는다
    # 만약 temp의 길이가 최대 묶음만큼 채워졌다면 break하여 조기 종료한다.
    for i in range(0, t * m):
        # 진수 변환할 때 사용할 빈 문자열
        temp_str = ''
        
        # 한자리씩 잘라서 넣은 배열의 길이가 최대묶음 길이를 충족시키면 break
        if len(temp) >= t * m : break

        # 2, 8, 16 진수는 변환하는 함수를 사용하였음
        if n == 2:
            temp.extend(list(str(bin(i))[2:]))
            
        elif n == 8:
            temp.extend(list(str(oct(i))[2:]))
            
        elif n == 16:
            temp.extend(list(str(hex(i))[2:]))
            
        else :
            # 나머지 진수는 계산해야함
            # 11 ~ 15진수에서는 10 ~ 15는 각각 대문자 A~F로 출력해야 한다.

            # 0부터 break되기 전 까지 n진수로 변환하여 temp배열에 append한다.
            # 이때, while의 조건식에 부합하지 않는 0은 temp에 바로 append한다.
            t1 = i
            if t1 == 0 :
                temp.append(temp_str + str(t1))
                continue
            # 진수 계산 반복문
            while (t1 > 0) :
                # t1을 n으로 나누었을 때, 나머지가 10 ~ 15 사이이면 -> 11 ~ 15진수에 해당함. 따라서 i + 55 식으로 대문자 아스키 코드 숫자로 만들어서 문자로 변환하여 추가.
                if t1 % n >= 10 and t1 % n <= 15:
                    temp_str =  temp_str + chr(t1 % n + 55)
                # 그렇지 않을 경우에는 나머지를 추가
                else : 
                    temp_str =  temp_str + str(t1 % n)
                # 다음 값을 계산하기 위해 몫 계산
                t1 = t1 // n
            # while문이 끝나면 문자열을 반대로 만들고 temp에 넣어줌.
            temp.extend(list(temp_str[::-1]))
            
    # temp 배열에서 내 순서인 경우에 숫자를 뽑아서 answer에 넣기
    # 나는 p번째임. -> temp 배열 안에서 내 순서는(1부터 count 한다.) . . . i % m으로 묶음에서의 인덱스 계산 후 + 1 하면 나의 순서임을 알 수 있음
    for i, item in enumerate(temp) :
         index= i % m + 1
        
         if len(answer) >= t :
                break
        
         if index == p:
                # 문자이면 대문자 변환
                if item.isalpha() :
                    answer = answer + str(item).upper()
                    continue
                # 아니면 item그대로 넣기
                answer = answer + str(item)

    return answer