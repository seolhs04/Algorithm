def solution(s):
    answer = []
    for idx in s :
        if answer:
            if answer[-1]==idx :
                answer.pop()
            else :
                answer.append(idx)
        else :
            answer.append(idx)
    return 0 if answer else 1