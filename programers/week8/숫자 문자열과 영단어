def solution(s):
    answer = ""
    dic = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, 
           "six" : 6,  "seven" : 7, "eight" : 8, "nine" : 9}
    
    temp = ""
    
        
    for i in range (0, len(s)) :
        
        if i == len(s) - 1 and s[i].isalpha():
            temp = temp + s[i]
            answer = answer + str(dic[temp])
        
        elif temp in dic :
            answer = answer + str(dic[temp])
            temp = ""
            
        if s[i].isalpha() :
            temp = temp + s[i]
            
        else :
            answer = answer + s[i]

    
    return int(answer)