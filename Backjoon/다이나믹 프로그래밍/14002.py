# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

# 예제 입력 1 
# 6
# 10 20 10 30 20 50
# 예제 출력 1 
# 4
# 10 20 30 50

def main():
    N=int(input())
    value=list(map(int, input().split(' ')))
    dp=[1]*N

    for i in range(N):
        C=0
        for j in range(i):
            if value[i]>value[j] and C<dp[j]:
                C=dp[j]
        dp[i]=C+1

    num=max(dp)
    print(num)
    result=[]
    for i in range(N-1,-1,-1):
        if dp[i]==num:
            result.append(value[i])
            num-=1
    
    result.reverse()
    print(*result,sep=' ')
    


main()