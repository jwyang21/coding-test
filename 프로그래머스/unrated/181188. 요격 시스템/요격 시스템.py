def solution(targets):
    targets.sort(key = lambda x: x[1])
    e = 0
    s = 0
    answer = 0
    for target in targets:
        current_s, current_e = target[0], target[1]
        if current_s >= e:
            answer += 1
            e = current_e
    return answer