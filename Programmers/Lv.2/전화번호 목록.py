def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        if i == len(phone_book)-1:
            break
            
        pre = phone_book[i]
        next = phone_book[i+1]
        
        if pre in next and next.index(pre) == 0:
            return False

    return True