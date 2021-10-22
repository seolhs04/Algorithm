def solution(n, m):
    return (최대공약수(n,m),최소공배수(n,m))
def 최대공약수(n,m):
    return m if n%m ==0 else 최대공약수(m,n%m)
def 최소공배수(n,m):
    return (n*m)/최대공약수(n,m)