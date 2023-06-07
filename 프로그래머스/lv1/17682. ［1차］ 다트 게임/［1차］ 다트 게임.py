def solution(dartResult):
    score = []
    curr = ''
    for i in dartResult:
        if i.isnumeric():
            curr += i
        elif i == 'S':
            curr = int(curr)
            score.append(curr)
            curr = ''
        elif i == 'D':
            curr = int(curr) ** 2
            score.append(curr)
            curr = ''
        elif i == 'T':
            curr = int(curr) ** 3
            score.append(curr)
            curr = ''
        elif i == '*':
            if len(score) >= 2:
                score[-1] = score[-1]*2
                score[-2] = score[-2]*2
            else:
                score[-1] = score[-1]*2
        elif i == '#':
            score[-1] = score[-1] * (-1)
        else:
            pass
    answer = sum(score)
    
    return answer