from collections import Counter

def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    
    num_1 = Counter(bin_n)['1'] 
    
    
    while True:
        
        n = n + 1
        
        bin_next = bin(n)[2:]
        
        num_1_bin_next = Counter(bin_next)['1']
        
        if num_1 == num_1_bin_next:
            answer = int(bin_next, 2)
            break

    return answer