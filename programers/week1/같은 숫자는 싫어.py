# 같은 숫자는 싫어

def solution(arr):
    top = 0
    temp = 0
    answer = []
    
    while 1 :
        
        if top > len(arr) - 1 : break
    
        # 초기 조건
        if top == 0 :
            answer.append(arr[top]) 
            temp = arr[top]
            top = top + 1
        
        
        else :
            if temp == arr[top] : 
                temp = arr[top]
                top = top + 1
            
            else :
                answer.append(arr[top])
                temp = arr[top]
                top = top + 1       
    
    return answer


# 테스트
arr = [1, 1, 3, 3, 0, 1, 1]
result = solution(arr)
print(result)