'''

풀이시간 : 29분
시간복잡도 : n^2

'''

def change_to_binary(arr, n):
    for i in range(0, len(arr)):
        arr[i] = bin(arr[i])[2:]
        
    for i in range(0, len(arr)):
        while(len(arr[i]) != n):
            arr[i] = "0" + str(arr[i])    

def compare(a, b) :
    if a == "0" and b == "0":
        return " "
    else :
        return "#"
        
def solution(n, arr1, arr2):
    answer = []
    change_to_binary(arr1, n)
    change_to_binary(arr2, n)
    
    for i in range(0, len(arr1)):
        temp = ""
        for j in range(0, n):
            temp = temp + compare(arr1[i][j], arr2[i][j])

        answer.append(temp)

    return answer