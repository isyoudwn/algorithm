from collections import Counter

def solution(str1, str2):
    str1_array = []
    str2_array = []
    
    union_dic = {}
    inter_dic = {}
    
    # str을 2개씩 끊음
    for i in range(0, len(str1) - 1) :
        text = str1[i] + str1[i + 1]
        str1_array.append(text)
        
    for i in range(0, len(str2) - 1) :
        text = str2[i] + str2[i + 1]
        str2_array.append(text)
    
    # 공백 제거, 문자열이 아닌 것을 포함하면 제거, 대문자인 것을 소문자로 만들어줌
    str1_array = [item.lower() for item in str1_array if item.isalpha()]
    str2_array = [item.lower() for item in str2_array if item.isalpha()]
    
    # str_array에서 Counter로 각 문자열이 얼마나 나왔는지 확인
    str1_dic = Counter(str1_array)
    str2_dic = Counter(str2_array)
    
    # 합집합 딕셔너리 만들기
    # 두 딕셔너리의 key를 확인해서, 합집합 딕셔너리의 key로 넣음 => 이때, 중복되는 것이 있으면 value를 확인해서 큰 값을 넣음.
    for k, v in str1_dic.items() :
        if k in str2_dic :
            union_dic[k] = max(str1_dic[k], str2_dic[k])
        else :
            union_dic[k] = str1_dic[k]
    
    for k, v in str2_dic.items() :
        if k not in union_dic :
            union_dic[k] = str2_dic[k]

    # 교집합 딕셔너리 만들기
    # 두 딕셔너리의 key를 확인해서, 같은 것이 존재하면 교집합 딕셔너리의 key로 넣음. 그리고, 그것 중 작은 값을 value로 넣음
    for k, v in str1_dic.items() :
        if k in str2_dic :
            inter_dic[k] = min(str1_dic[k], str2_dic[k])

    # union_dic가 비어있고, inter_dic 또한 비어있으면 => 65536을 return (1로 취급하기 때문ㅇ)
    if not union_dic and not inter_dic :
        return 65536
    
    union_cnt = 0
    inter_cnt = 0
    
    # 합집합 딕셔너리의 모든 원소를 더함
    for k, v in union_dic.items():
        union_cnt += v

    # 교집합 딕셔너리의 모든 원소를 더함
    for k, v in inter_dic.items():
        inter_cnt += v

    # 정수로 출력
    return int((inter_cnt / union_cnt) * 65536)