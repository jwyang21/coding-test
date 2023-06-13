def solution(book_time):
    # https://kcw0360.tistory.com/10
    
    answer = 0
    
    check = [0] * 1440
    
    for tmp in book_time:
        start, end = tmp[0], tmp[1]
        sh, sm = map(int, tmp[0].split(':'))
        eh, em = map(int, tmp[1].split(':'))
        start = sh * 60 + sm
        end = eh * 60 + em + 10
        
        if end > 1440:
            end = 1440
            
        for idx in range(start, end):
            check[idx] += 1
            
    answer = max(check)    
    
    return answer