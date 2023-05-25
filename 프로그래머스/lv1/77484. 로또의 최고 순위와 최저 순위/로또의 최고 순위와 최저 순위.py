import numpy as np

def solution(lottos, win_nums):
    d = {6:1,5:2,4:3,3:4,2:5,1:6,0:6} # key: 일치하는 번호 개수 # value: 순위
    
    min_number = len(np.intersect1d(lottos, win_nums))
    
    if min_number in list(d.keys()):
        min_rank = d[min_number]
    else:
        min_rank = 6
        
    unknown = lottos.count(0)
    max_number = min_number + unknown
    max_rank = d[max_number]
    answer = [max_rank, min_rank]
    
    return answer