def solution(n):
    dct = {0: '수', 1: '박'}
    answer = ''
    for i in range(n):
        i = i % 2
        answer += dct[i]
    return answer