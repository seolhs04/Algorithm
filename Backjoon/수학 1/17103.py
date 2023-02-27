# 문제
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

# 출력
# 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

from sys import stdin
def main():
    isPrime = [False,True]*500000
    for i in range(3,1000,2):
        if isPrime[i]:
            j = 2
            while i*j<len(isPrime):
                isPrime[i*j]=False
                j+=1
    isPrime[1]=False
    isPrime[2]=True

    count = int(stdin.readline()[:-1])

    for _ in range(count):
        value = int(stdin.readline()[:-1])
        cnt=0
        for i in range(value//2+1):
            if isPrime[i] and isPrime[value-i]: cnt+=1
        print(cnt)

main()