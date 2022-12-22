# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 5
# 5
# 4
# 3
# 2
# 1
# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5

import sys
def main():
    cnt = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(cnt)]
    for i in sorted(arr): sys.stdout.write(str(i)+'\n') 
    

def quick_sort(arr:list,start:int,end:int):
    if start>=end: return
    pivot = (start+end)//2
    left = start
    right = end
    while left<=right:
        while arr[left]<arr[pivot]: left+=1
        while arr[right]>arr[pivot]: right-=1
        if left<=right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1

    quick_sort(arr,start,pivot)
    quick_sort(arr,pivot+1,end)
    


main()