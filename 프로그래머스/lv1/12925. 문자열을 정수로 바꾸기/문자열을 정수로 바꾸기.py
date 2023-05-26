def solution(s):
    if s[0] == '+':
        s = s[1:]
        answer = int(s)
    elif s[0] == '-':
        s = s[1:]
        answer = (-1) * int(s)
    else:
        answer = int(s)
    return answer