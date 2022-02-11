import math

def solution(n):
    answer = 0
    
    while n>1 :
        if n%2 ==0 and n!=2:
            n-=1
        if math.sqrt(n) - int(math.sqrt(n))==0:
            n-=1
        if isPrime(n) == True :
            answer+=1
        n-=1
    
    return answer

def isPrime(num):
    if(num<2):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False
    return True