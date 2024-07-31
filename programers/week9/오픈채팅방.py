# O(n)
# 20분소요

def changeUserData(record, userDict) :
    for i in record:
        
        temp = i.split(' ')
        
        if temp[0] != 'Leave':
            userId = temp[1]
            nickName = temp[2]
        
        userDict[userId] = nickName
            
    
def changeToResultLog(record, userDict, result):
    for i in record:
        temp = i.split()
        if temp[0] != 'Change':
            userId = temp[1]
            nickName = userDict[userId]
            
            if temp[0] == 'Enter':
                result.append(nickName+"님이 들어왔습니다.")
            elif temp[0] == 'Leave':
                result.append(nickName+"님이 나갔습니다.")
            else :
                result.append(nickName+"님이 들어왔습니다.")
            
        
def solution(record):
    answer = []
    userDict = {}
    changeUserData(record, userDict)
    changeToResultLog(record, userDict, answer)
    
    
    
    return answer