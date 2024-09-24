from collections import deque

def solution(operations):
    answer = []
    queue = deque()

    for o in operations:
        # print(o)
        if o == "D 1":
            if len(queue) < 1:
                continue
            queue.pop()
        elif o == "D -1":
            if len(queue) < 1:
                continue
            queue.popleft()
        else:
            number = int(o[2:])
            if len(queue) < 1:
                # print('1')
                queue.append(number)
            elif queue[0] > number:
                # print('2')
                queue.appendleft(number)
            elif queue[len(queue) - 1] < number:
                # print('3')
                queue.append(number)
            else:
                # print('4')
                a = queue.pop()
                queue.append(number)
                queue.append(a)
                
        # print(queue)
    if len(queue) < 1:
        answer = [0, 0]
        
    else:
        answer = [queue[len(queue)-1], queue[0]]
    
    return answer