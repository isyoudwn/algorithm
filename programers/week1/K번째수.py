# K번째수

def solution(array, commands):
    answer = []
    temp = []
    
    for i in range(0, len(commands)) :
        command = commands[i]
        start = command[0] - 1
        end = command[1] - 1
        k = command[2]
        
        temp = array[start:end+1]
        
        temp.sort()
        
        kNumber = temp[k - 1]
        
        answer.append(kNumber)
    
    return answer

# 테스트

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

result = solution(array, commands)

print(result)