def solution(n):
    if int(n ** (1/2)) == n ** (1/2):
        answer = ((n ** (1/2))+1)**2
    else:
        answer = -1
    return answer