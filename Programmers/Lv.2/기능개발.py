import math

def solution(progresses, speeds):
    answer = []
    
    result = list(map(lambda x: 100-x,progresses))
    for i in range(0,len(result)) :
        result[i] = math.ceil(result[i]/speeds[i])
    
    pre = 0
    while len(result)>0 :
        if result[0] <= pre :
            answer[len(answer)-1]+=1
        else:
            answer.append(1)
        
        if result[0]>pre :
            pre = result.pop(0)
        else:
            result.pop(0)
        
    return answer