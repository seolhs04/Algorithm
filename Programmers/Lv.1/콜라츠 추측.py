def solution(num):
    answer = 0
    count = 0
    while(num != 1):
        num = collatz(num)
        count += 1
        answer = count
        if(count == 500):
            answer = -1
            break
    return answer

def collatz(num):
    if(num%2 == 0):
        num = int(num/2)
    else:
        num = num*3 + 1
    return num