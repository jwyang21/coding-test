def solution(nums):
    num_pick = len(nums)/2
    
    uniques = list(set(nums))
    if len(uniques) >= num_pick:
        result = num_pick
    else:
        result = len(uniques)
    
    result = int(result)
    
    return result