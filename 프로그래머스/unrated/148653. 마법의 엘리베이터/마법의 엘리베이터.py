def solution(storey):
    
    # https://mag1c.tistory.com/166
    # 5일 경우, 다음 자리 수가 5 이상이면 올라가고, 4 이하면 내려감
    
    answer = 0
    
    tmp = str(storey)
    arr = [int(i) for i in tmp]
    answer = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > 5:
            answer += 10-arr[i]
            if i==0:
                answer += 1
            else:
                arr[i-1] += 1
        elif arr[i]==5 and i>0 and arr[i-1]>=5:
            arr[i-1] += 1
            answer += 5
        else:
            answer += arr[i]
            
    return answer