
def solution(phone_book):
    answer = True
    
    # 사전식으로 정렬 됨
    # [1, 2, 3 , 10] -> [1, 10, 2, 3]
    # index가 index + 1의 접두사이면, 반드시 그 뒤에 존재할 것.
    phone_book.sort()
    
    for i in range(0, len(phone_book)) :
        # base-case
        if i == len(phone_book) - 1 :
            return True
        # phone_book[i] 와 phone_book[i + 1]을 phone_book[i]의 길이만큼 슬라이싱 후 같은지 비교 => 접두사 비교
        if phone_book[i] == (phone_book[i + 1])[0:len(phone_book[i])] :
            return False
    
    return answer

