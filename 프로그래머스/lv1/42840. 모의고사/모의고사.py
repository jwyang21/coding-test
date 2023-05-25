import numpy as np

def solution(answers):
    answer_cnt = {1:0, 2:0, 3:0}
    
    first = [1, 2, 3, 4, 5]
    
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if first[i%5] == answers[i]:
            answer_cnt[1] += 1
        if second[i%8] == answers[i]:
            answer_cnt[2] += 1
        if third[i%10] == answers[i]:
            answer_cnt[3] += 1
            
    max_cnt = max(list(answer_cnt.values()))
    
    answer = []
    for i in range(len(answer_cnt)):
        if list(answer_cnt.values())[i] == max_cnt:
            answer.append(list(answer_cnt.keys())[i])
    
    return sorted(answer)