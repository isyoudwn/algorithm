# 30분 소요
# '(' 를 stack에 넣음 -> 문자열에서 ')' 가 나오면 stack에서 '(' 를 뺀다.
# 문자열 탐색이 끝나면 stack이 비어야 있어야함.
# 문자열이 안 끝났는데 pop을 해야하는 경우 짝이 맞지 않음.

def solution(s):
    answer = True
    
    stack = []
    
    for i in range(0, len(s)) :        
        
        # pop을 해야하는데 stack이 비어있는 경우, 옳지 않은 괄호.
        if s[i] == ")" and len(stack) == 0:
            answer = False
            break
        # '('는 stack에 넣음.
        elif s[i] == "(" :
            stack.append(s)
        # ')'가 나올 경우 stack에서 '('를 뺀다. -> 짝을 찾았기 때문
        elif s[i] == ")" :
            stack.pop()

        # 위 조건 외 다른 조건들 또한 옳지 않은 경우임.
        else : 
            answer = False
        
    # 문자열 탐색이 끝났는데, stack이 비어있지 않으면 False
    if len(stack) != 0 :
        answer = False
    
    return answer