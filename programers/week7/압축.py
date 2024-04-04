def solution(msg):
    answer = []
    word = ""
    
    dic = {}
    number = 1
    
    # 딕셔너리를 A-Z까지 초기화 -> 아스키 코드 사용
    # 알파벳을 딕셔너리의 키로 사용, number를 색인 번호로 사용
    for i in range(65, 91):
        dic[chr(i)] = number
        number = number + 1

    # 들어온 msg의 길이 만큼 반복 수행
    # i부터 시작해서 ~ . . . i를 첫문자로 시작해서. . . 다음 인덱스를 탐색하면서 최대로 만들 수 있는 가장 긴 문자열이 사전에 등록되어 있는지 확인
    # 등록되지 않았으면 사전에 새롭게 추가한다.
    i = 0
    while (i < len(msg)):
        word = msg[i]
        
        # 마지막 글자부터 찾을 경우. . . 이 글자 단독이라는 뜻! 이 글자가 사전에 포함 되었으면 answer에 색인번호 추가.
        if i == len(msg) - 1:
            if word in dic:
                answer.append(dic[word])
        
        for j in range(i + 1, len(msg)):
            # temp는 시작 글자 + 다음 글자 (즉, 사전에 있는지 없는지 검증을 아직 하지 않은 글자)
            temp = word + msg[j]
            
            if j == len(msg) - 1:
                if temp in dic:
                    answer.append(dic[temp])
            # 현재 인덱스를 j(i ~ j까지는 사전에 등록되어있기 때문에 판별대상이 아니라서)로 바꿔주어야함 => 인덱스 위치를 옮겨준다.
            if temp in dic :
                word = temp
                i = j
            # 딕셔너리에 temp가 없으면, word의 색인번호를 answer에 넣고 사전에 새로운 단어를 등록해준다.
            else :
                answer.append(dic[word])
                #사전에 등록
                dic[temp] = list(dic.values())[-1] + 1
                break
        #인덱스 증가
        i = i + 1
    
            
    
    return answer