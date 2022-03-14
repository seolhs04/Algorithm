def solution(numbers, target):
    answer = 0
    
    def dfs(value, current):
        nonlocal answer
        if current == len(numbers) :
            if value == target :
                answer += 1
            return
        
        dfs(value+numbers[current], current+1)
        dfs(value-numbers[current], current+1)
            
    dfs(0, 0)

    return answer