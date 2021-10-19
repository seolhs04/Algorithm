def solution(x):
    sum = 0
    for i in range(0,len(str(x))):
        sum+=int(str(x)[i])
    if(x % sum == 0):
        answer = True
    else:
        answer = False
    
    return answer