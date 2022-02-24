def solution(n, lost, reserve):
    _lost = list(set(lost) - set(reserve))
    _reserve = list(set(reserve) - set(lost))
    
    answer = n - len(_lost)
    for i in _lost:
        if i - 1 in _reserve:
            answer += 1 
            _reserve.remove(i - 1)
        elif i + 1 in _reserve: 
            answer += 1
            _reserve.remove(i + 1) 
            
    return answer