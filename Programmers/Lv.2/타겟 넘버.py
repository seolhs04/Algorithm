from collections import deque

def solution(numbers, target):
    answer = 0
    
    # dfs
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

# bfs
def bfs(numbers, target):
    queue = deque([[numbers[0],0],[-numbers[0],0]])
    answer = 0
    while queue :
        num, i = queue.popleft()
        if i+1 == len(numbers) :
            if num == target : answer+=1
        else :
            queue.append([num+numbers[i+1],i+1])
            queue.append([num-numbers[i+1],i+1])
    
    return answer