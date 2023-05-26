def solution(a, b):
    tmp = sorted([a, b])
    a, b = tmp[0], tmp[1]
    answer = 0
    if a==b:
        return a
    else:
        for i in range(a, b+1):
            answer += i
    return answer