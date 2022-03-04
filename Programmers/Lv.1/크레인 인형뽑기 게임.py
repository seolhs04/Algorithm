def solution(board, moves):
    answer = 0
    arr = []
    cnt = 0
    while cnt<len(moves) :
        for i in board :
            if i[moves[cnt]-1] != 0 :
                arr.append(i[moves[cnt]-1])
                board[board.index(i)][moves[cnt]-1] = 0
                break
        if len(arr) >= 2 and arr[-1] == arr[-2]:
            answer += 2
            arr = arr[:-2]
        cnt += 1
        
    return answer