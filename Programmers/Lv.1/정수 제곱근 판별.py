import numpy as np

def solution(n):
    answer = 0
    if(np.sqrt(n)-int(np.sqrt(n)) == 0.0):
        answer = (int(np.sqrt(n))+1)**2
    else:
        answer = -1
    
    return answer