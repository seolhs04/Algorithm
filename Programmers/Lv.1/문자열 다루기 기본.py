def solution(s):
    if len(s) == 4:
        return checkNum(s)
    elif len(s) == 6:
        return checkNum(s)
    else:
        return False
    
def checkNum(s):
    try:
        int(s)
        return True
    except:
        return False