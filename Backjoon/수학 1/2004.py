# 문제
#  
# $n \choose m$의 끝자리 
# $0$의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 
# $n$, 
# $m$ (
# $0 <= m <= n <= 2,000,000,000$, 
# $n \ne 0$)이 들어온다.

# 출력
# 첫째 줄에 
# $n \choose m$의 끝자리 
# $0$의 개수를 출력한다.

# 예제 입력 1 
# 25 12
# 예제 출력 1 
# 2

# n!/(n-m)! * m!
def main():
    n,m = map(int,input().split(' '))
    print(min(cal(n,2)-cal(m,2)-cal(n-m,2),cal(n,5)-cal(m,5)-cal(n-m,5)))

def cal(num, targetNum):
    cnt=0
    while num != 0:
        num //= targetNum
        cnt += num
    return int(cnt)

main()