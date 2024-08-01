# O(n^2)
# 50분 소요

def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)

    
    for m in moves: 
        for i in range(0, n):
            if board[i][m-1] == 0 :
                continue
            else:
                temp = board[i][m-1]
                board[i][m-1] = 0

                if len(stack) != 0 and stack[len(stack)-1] == temp:
                    stack.pop()
                    answer += 2
                else :
                    stack.append(temp)
                break
        
    return answer