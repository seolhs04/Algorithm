def main():
    value = int(input())
    cnt=0
    while value != 0:
            value //= 5
            cnt += value
    print(cnt)

main()