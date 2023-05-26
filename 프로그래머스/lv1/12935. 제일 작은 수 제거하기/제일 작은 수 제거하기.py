def solution(arr):
    min_index = arr.index(min(arr))
    del arr[min_index]
    if len(arr) == 0:
        arr = [-1]
    return arr