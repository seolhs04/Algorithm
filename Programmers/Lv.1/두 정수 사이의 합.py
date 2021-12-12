import numpy as np

def solution(a, b):
    arr = np.arange(a,b+1) if a<=b else np.arange(b,a+1)
    
    return int(np.sum(arr))