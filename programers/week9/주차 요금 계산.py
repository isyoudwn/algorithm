# 약 1시간 소요

import math

def solution(fees, records):
    answer = []
    tempDict = {}
    resultDict = {}
    
    basicTime = fees[0]
    basicFee = fees[1]
    formTime = fees[2]
    formFee = fees[3]
    
    
    # IN - OUT해서 시간을 분 단위로 계산
    for value in records :
        time = value.split(' ')[0]
        id = value.split(' ')[1]
        info = value.split(' ')[2]
        
        if id in tempDict:
            temp = time.split(':')
            
            t = int(temp[0]) - int(tempDict[id][0])
            m = int(temp[1]) - int(tempDict[id][1])
            
            total = (t * 60) + m
            
            del tempDict[id]
            
            if id in resultDict:
                resultDict[id] = resultDict[id] + total
            else :
                resultDict[id] = total
            
        else :
            tempDict[id] = time.split(':')
    
    
    # 출차 정보 없는 애들 계산
    if len(tempDict) != 0:
        for k, v in tempDict.items():
            t = 23 - int(v[0])
            m = 59 - int(v[1])
            
            total = (t * 60) + m
            
            if k in resultDict:
                resultDict[k] = resultDict[k] + total
            else :
                resultDict[k] = total
                
    # 주차요금 계산
    for k, v in resultDict.items() :
        
        if v <= basicTime:
            resultDict[k] = basicFee
            continue
        
        resultDict[k] = basicFee + math.ceil( (v - basicTime) / formTime) * formFee
    
    # 차량 번호 오름차순 정렬
    result = sorted(resultDict.items(), key= lambda x:x[0], reverse = False)
    
    # answer에 append
    for r in result :
        answer.append(r[1])
        
    return answer