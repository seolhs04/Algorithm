def solution(s):
    answer = ''
    count = 0
    for i in s:
        count = 0 if(i==' ') else count+1
        answer += i.upper() if(count%2!=0) else i.lower()
        
    return answer