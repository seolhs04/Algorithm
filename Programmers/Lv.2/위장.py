def solution(clothes):
    answer = 1
    dic = {}
    for cloth, category in clothes :
        if category not in dic :
            dic[category] = []
        dic[category] += [cloth]
        
    for i in dic.values() :
        answer *= len(i)+1
    
    return answer-1