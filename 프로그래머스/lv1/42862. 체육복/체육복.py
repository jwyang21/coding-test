def solution(n, lost, reserve):
    reserve_ = set(reserve) - set(lost)
    lost_ = set(lost) - set(reserve)
    
    for x in reserve_:
        if x-1 in lost_:
            lost_.remove(x-1)
        elif x+1 in lost_:
            lost_.remove(x+1)
        else:
            pass
    return n - len(lost_)
    