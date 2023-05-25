import numpy as np
def solution(N, stages):
    failure_cnt = [0]*N
    for i in range(N):
        num_players = (np.array(stages)>=(i+1)).sum()
        failure_cnt[i] = stages.count(i+1) / num_players
    failure_dct = dict(zip(range(1,N+1), failure_cnt))
    sorted_failure_dct = sorted(failure_dct.items(), key = lambda item: item[1], reverse = True)
    answer = [sorted_failure_dct[i][0] for i in range(len(sorted_failure_dct))]
    return answer