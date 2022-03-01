def solution(n):
    answer = ''
    
    while n:
        if n%3!=0 :
            answer = str(n%3) + answer
        else :
            answer = '4' + answer
            n -= 1
        n = n // 3
    
    return answer