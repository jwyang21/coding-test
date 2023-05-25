def solution(k, score):
    answer = []
    tmp = []

    for i in range(len(score)):
        current_score = score[i]
        tmp.append(current_score)
        tmp = sorted(tmp)
        if len(tmp) > k:
            tmp = tmp[-k:]
        answer.append(tmp[0])
    return answer