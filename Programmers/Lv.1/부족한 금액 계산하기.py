def solution(price, money, count):
    answer = 0
    cnt = 1
    while cnt<=count :
        answer += cnt*price
        cnt+=1
    
    return 0 if answer - money < 0 else answer - money