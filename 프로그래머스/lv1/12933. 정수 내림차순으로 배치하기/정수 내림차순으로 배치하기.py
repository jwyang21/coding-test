def solution(n):
    l = sorted([int(x) for x in str(n)], reverse = True)
    l_ = [str(x) for x in l]
    answer = int(''.join(l_))
    return answer