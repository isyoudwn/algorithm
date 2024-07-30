def formatting(files, tempArr) :
    
    for i in range(0, len(files)):
        head = ""
        number = ""
        flag = False
        
        for j in range(0, len(files[i])):
            if j == len(files[i]) - 1:
                number += files[i][j]
                tempArr.append([files[i], head, int(number)])
                break
                
            elif files[i][j].isdecimal() == False and flag == True:
                tempArr.append([files[i], head, int(number)])
                break
                
            elif files[i][j].isdecimal() == False:
                head += files[i][j].lower()

            else :
                flag = True
                number += files[i][j]
            

def formattingToAnswer(answer, arr) :
    for i in arr:
        answer.append(i[0])


def solution(files):
    answer = []
    tempArr = []
    
    formatting(files, tempArr)
    
    arr = sorted(tempArr, key=lambda x:(x[1], x[2]))
    
    formattingToAnswer(answer, arr)
    
    
    return answer