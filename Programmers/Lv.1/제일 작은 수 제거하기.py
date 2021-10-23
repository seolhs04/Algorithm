def solution(arr):
    arr.remove(sorted(arr).pop(0))
    if(len(arr) == 0):
        arr.append(-1)
    return arr