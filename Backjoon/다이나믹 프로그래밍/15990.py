# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

# 1+2+1
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 100,000보다 작거나 같다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 3
# 4
# 7
# 10
# 예제 출력 1 
# 3
# 9
# 27

from sys import stdin
def main():
    loop = int(stdin.readline()[:-1])
    values=[]

    for _ in range(loop):
        values.append(int(stdin.readline()[:-1]))

    arr= list([0,0,0] for _ in range(max(values)+1))
    arr[1],arr[2],arr[3] = [1,0,0],[0,1,0],[1,1,1]

    for i in range(4,max(values)+1):
        arr[i][0]=(arr[i-1][1]+arr[i-1][2])%1000000009
        arr[i][1]=(arr[i-2][0]+arr[i-2][2])%1000000009
        arr[i][2]=(arr[i-3][0]+arr[i-3][1])%1000000009
            
    for j in values:
        print(sum(arr[j])%1000000009)

main()