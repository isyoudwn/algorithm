def returnIndex(value) :
    if value == 'R' or value == 'T':
        return 1
    if value == 'C' or value == 'F':
        return 2
    if value == 'J' or value == 'M':
        return 3
    if value == 'A' or value == 'N':
        return 4


def solution(survey, choices):
    answer = ''
    
    personality = {
                    1 : {'R' : 0, 'T' : 0}, 
                    2 : {'C' : 0, 'F' : 0},
                    3 : {'J' : 0, 'M' : 0},
                    4 : {'A' : 0, 'N' : 0},
                }
    
    choice_menu = {
        1 : 3,
        2 : 2,
        3 : 1,
        4 : 0,
        5 : 1,
        6 : 2,
        7 : 3
    }
    
    

    for i in range(0, len(survey)) :
        if choices[i] >= 5 :
            personality[returnIndex(survey[i][1])][survey[i][1]] = personality[returnIndex(survey[i][1])][survey[i][1]] + choice_menu[choices[i]]
        else :
            personality[returnIndex(survey[i][0])][survey[i][0]] = personality[returnIndex(survey[i][0])][survey[i][0]] + choice_menu[choices[i]]
        
    for key, value in personality.items() :
        max_key = max(value, key = value.get)
        answer = answer + max_key

    return answer