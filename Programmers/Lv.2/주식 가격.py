def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        answer.append(0)
        for j in range(i+1,len(prices)):
            answer[i] += 1
            if prices[i]>prices[j] :
                break
                
    return answer