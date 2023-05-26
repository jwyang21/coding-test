def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif 0 < i <= len(arr)-1:
            if arr[i] != arr[i-1]:
                answer.append(arr[i])
        else: 
            pass
    return answer