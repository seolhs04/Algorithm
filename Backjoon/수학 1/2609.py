# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 예제 입력 1 
# 24 18
# 예제 출력 1 
# 6
# 72

from sys import stdin
def main():
    a,b = map(int, stdin.readline()[:-1].split(' '))
    print(최대공약수(a,b))
    print(최소공배수(a,b))
    
def 최대공약수(n,m):
    return m if n%m == 0 else 최대공약수(m,n%m)
def 최소공배수(n,m):
    return int((n*m)/최대공약수(n,m))

main()