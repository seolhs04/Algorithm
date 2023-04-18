from itertools import product

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))

list(map(lambda x: print(' '.join(list(map(str, list(x))))), product(lst, repeat=M)))
