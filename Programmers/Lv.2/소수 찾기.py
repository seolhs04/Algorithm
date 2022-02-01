import math
from itertools import permutations

def solution(numbers):
    items = []
    for i in range(1, len(list(numbers))+1):
        items += list(map(''.join, permutations(list(numbers), i)))    
    
    items = list(map(lambda x: int(x), items))
    items = set(items)
    items = list(filter(isPrime, items))
    
    return len(items)
    
def isPrime(num):
    if(num<2):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False
    return True