# O(n^3)
# 4시간 소요

def solution(arr1, arr2):
    # answer 배열의 행을 미리 만들어 줌
    # answer 배열의 행 개수는 arr1의 행 개수와 같음
    answer = [[] for row in range(0, len(arr1))]
    # arr2의 열 수 미리 계산
    arr2_col = len(arr2[0])
    
    # arr1을 기준으로 탐색 -> arr1이 끝나면 반복문 종료
    for i, arr1_row in enumerate(arr1) :

        # arr1의 행은 고정되고, arr2의 열을 탐색해야 함.
        # arr1의 i행 * arr2의 j열 로직
        for j in range(0, arr2_col):
            # 행과 열을 곱한 값을 초기화 하는 부분
            ans = 0
            # 계산을 arr1의 행 길이 만큼 반복해야 함
            # arr1 열과 arr2의 행은 같아야 함 -> k
            # arr1의 행은 i로 고정됨
            # arr2의 열은 j로 고정됨
            for k in range(0, len(arr1_row)):
                ans =  ans + arr1[i][k] * arr2[k][j]
            # 계산 후 answer의 i행에 append -> answer의 행은 arr1의 행의 개수와 같기 때문.
            answer[i].append(ans)
        
    return answer