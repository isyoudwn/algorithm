def solution(n,a,b):
    answer = 0

    # list에 사람 넣기
    li = [k for k in range(1, n + 1)]
    
    
    for i in range(1, 21):
        temp = []
        for j in range(0, len(li), 2):
            if (li[j] == a and li[j+1] == b) or (li[j] == b and li[j+1] == a):
                return i
            elif li[j] == a or li[j+1] == a:
                temp.append(a)
            elif li[j] == b or li[j+1] == b :
                temp.append(b)
            else:
                temp.append(li[j])
        li = temp
