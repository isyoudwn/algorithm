
def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    privacies_dict = {}
    result_day = []
    
    # 개인정보 : 1 ~ n 번 분류
    # 개인정보 보관 유효기간이 정해져있음
    # 어떤 약관으로 수집됐는지 알고있음
    # 유효기간 전까지만 보관 가능 -> 이후에 파기
    # 오늘 파기해야할 개인정보 번호 구하기
    # 모든 달은 28일까지

    for i in range(0, len(terms)):
        t = terms[i].split(' ')
        terms_dict[t[0]] = int(t[1])

    for idx, p in enumerate(privacies):
        temp = p.split()
        privacies_dict[idx] = list(temp[0].split('.'))
        privacies_dict[idx].append(temp[1])
        
    for key, value in privacies_dict.items():
        temp = int(value[1]) + terms_dict[value[3]]
        
        if temp > 12:
            value[0] = str(int(value[0]) + temp // 12)
    
            if temp % 12 > 9:
                value[1] = str(temp % 12)
            else:
                    value[1] = '0' + str(temp % 12)
        else:
            if temp > 9:
                value[1] = str(temp)
            else:
                value[1] = '0' + str(temp)
        
        if value[1] == '00':
            value[0] = str(int(value[0]) - 1)
            value[1] = '12'
        
        result_day.append(''.join(value[:3]))
        
    today = today.split('.')
    today = ''.join(today)
    
    today = int(today)
    result_day = list(map(int, result_day))

    for idx, value in enumerate(result_day):
        if value <= today:
            answer.append(idx + 1)
    answer.sort()
        
    return answer