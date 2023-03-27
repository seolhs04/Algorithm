# 문제
# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

# 출력
# 첫째 줄에 경우의 수를 출력한다.

# 예제 입력 1
# 2
# 예제 출력 1
# 3

def main():
    N = int(input())
    dp = [0 for _ in range(31)]
    dp[2] = 3

    for i in range(4, 31, 2):
        dp[i] = 3 * dp[i - 2] + 2
        for j in range(4, i, 2):
            dp[i] += 2 * dp[i - j]

    print(dp[N])


main()
