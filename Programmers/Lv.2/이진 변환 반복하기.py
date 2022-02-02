def solution(s):
    answer = [0,0]
    
    while(s != '1'):
        answer[1] += trans(s)[0]
        s = trans(s)[1]
        answer[0] += 1
    
    return answer

def trans(str):
    zeroCnt = str.count('0')
    result = format(len(str)-zeroCnt, 'b')
    
    return [zeroCnt, result]