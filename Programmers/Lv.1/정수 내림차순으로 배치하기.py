def solution(n):
    a = sorted(list(str(n)))
    a.reverse()
    return int(''.join(a))