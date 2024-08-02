# 1시간 소요

def step1(string) :
    return string.lower()


def step2(string) :
    text = ''
    for s in string:
        if s.isalpha() or s.isdigit() or s in ['-', '_', '.']:
            text += s
    return text


def step3(string) :
    text = ''
    # for s in string:
    #     if len(text) == 0:
    #         text += s
    #         continue
    #     if s == '.' and text[len(text) - 1] == '.':
    #         continue
    #     text += s
        
    while '..' in string:
        string = string.replace('..', '.')
        
    text = string
    
    return text


def step4(string) :
    text = ''
    for i in range(0, len(string)):
        if i == 0 and string[i] == '.':
            continue
        if i == len(string) - 1 and string[i] == '.':
            continue
        text += string[i]
    return text


def step6(string):
    string = string[0:15]
    
    if string[-1] == '.':
        string = string[0:14]
    return string


def step7(string):
    last = string[-1]
    
    while len(string) < 3 :
        string += last
        
    return string
    

def solution(new_id):
    answer = ''
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    
    # step5
    if new_id == '' :
        new_id = 'a'
    
    # step6
    if len(new_id) >= 16 :
        new_id = step6(new_id)
        
    # step7
    if len(answer) <= 2:
        new_id = step7(new_id)
        
    answer = new_id

    return answer