# 입력
# 프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W). 

# 출력
# 프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

# 예제 입력 1 
# 2
# 6 12 10
# 30 50 72
# 예제 출력 1 
# 402
# 1203

def main():
    count = int(input())
    arr = []
    for _ in range(count):
        a,b,c = map(int,input().split())
        room_floor = a if c%a==0 else c%a
        room_num = c//a if c%a==0 else c//a + 1
        arr.append('{0}{1}'.format(room_floor, room_num if room_num>9 else '0'+str(room_num)))

    for i in arr:
        print(i)
main()

