# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
# 예제 출력 1 
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7
import sys
def main():
    cnt = int(sys.stdin.readline())
    arr = [0]*10000

    for _ in range(cnt):
        index = int(sys.stdin.readline())-1
        arr[index]+=1

    for i in range(len(arr)):
        if(arr[i]!=0):
            for _ in range(arr[i]):
                print(i+1)

main()