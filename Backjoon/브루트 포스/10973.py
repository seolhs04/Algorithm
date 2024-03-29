# 문제
# 1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 바로 이전에 오는 순열을 구하는 프로그램을 작성하시오.

# 사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

# N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10, 000)이 주어진다. 둘째 줄에 순열이 주어진다.

# 출력
# 첫째 줄에 입력으로 주어진 순열의 이전에 오는 순열을 출력한다. 만약, 사전순으로 가장 처음에 오는 순열인 경우에는 - 1을 출력한다.

# 예제 입력 1
# 4
# 1 2 3 4
# 예제 출력 1
# -1
# 예제 입력 2
# 5
# 5 4 3 2 1
# 예제 출력 2
# 5 4 3 1 2

N = int(input())
lst = list(map(int, input().split()))

key_idx = 0
target_idx = 0

for i in range(1, N):
    if lst[i-1] > lst[i]:
        key_idx = i-1

    if lst[key_idx] > lst[i]:
        target_idx = i

lst[key_idx], lst[target_idx] = lst[target_idx], lst[key_idx]

lst1 = lst[:key_idx + 1]
lst2 = sorted(lst[key_idx+1:], reverse=True)

if key_idx == target_idx:
    print(-1)
else:
    print(*list(lst1+lst2), sep=' ')
