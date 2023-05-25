def solution(n):
    tmp = ''
    while n > 0:
        tmp += str(n % 3)
        n = n//3
    
    answer = 0
    for i in range(len(tmp)):
        answer += (3**i) * int(tmp[(-1)*(i+1)])
    
    return answer