from collections import Counter

def solution(s):
    answer = []
    count_convert = 0
    count_delete_zero = 0
    
    
    while True:
        
        if s == "1":
            break
        
        cnt = Counter(s)
        
        if '0'in cnt:
            count_zero = cnt['0']
            count_delete_zero += count_zero
            s = s.replace('0', '')
            
        s = len(s)
        s = str(bin(int(s)))[2:]
        count_convert += 1
        
    answer = [count_convert, count_delete_zero]
    
    return answer