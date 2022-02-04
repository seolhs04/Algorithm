import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        if len(scoville) <= 1:
            answer = -1
            break
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville,first+2*second)
            answer += 1
        
    return answer