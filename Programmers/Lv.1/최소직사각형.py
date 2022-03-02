def solution(sizes):
    answer = [0,0]
    for i in sizes:
        i.sort()
        if i[0]>answer[0] : answer[0] = i[0]
        if i[1]>answer[1] : answer[1] = i[1]
                    
    return answer[0]*answer[1]