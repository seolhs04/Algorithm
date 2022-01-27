def solution(numbers):
    arr = [1,2,3,4,5,6,7,8,9]
    answer = sum(list(set(arr) - set(numbers)))
    
    return answer