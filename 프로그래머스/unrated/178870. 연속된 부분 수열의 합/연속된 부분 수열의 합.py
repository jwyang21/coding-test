from collections import deque
# https://velog.io/@wodnr0710/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.2-%EC%97%B0%EC%86%8D%EB%90%9C-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9
def solution(sequence, k):
    answer = []
    sequence += [0]
    
    q = deque()
    sum = 0
    start, end = 0, 0
    result = len(sequence)
    
    for i in range(len(sequence)):
        while sum > k:
            temp = q.popleft()
            sum -= temp
            start += 1
            
        # after while loop ends, record start and end if sum of sublist == k (only if end-start < result)
        if sum == k and end-start < result:
            # end-start < result: if there are multiple sublists, choose one with the smaller index
            answer = [start, end]
            result = end - start # length of sublist
        
        q.append(sequence[i]) # append sequence[i] to the right end of the queue
        sum += sequence[i]
        end = i # update end with i
    return answer
    