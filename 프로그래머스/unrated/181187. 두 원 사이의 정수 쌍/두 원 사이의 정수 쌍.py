import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        max_y = math.floor((r2**2-i**2)**0.5)
        if i>= r1:
            min_y = 0
        else:
            min_y = math.ceil((r1**2-i**2)**0.5)
        answer += (max_y-min_y+1)
    answer = answer*4

    return answer