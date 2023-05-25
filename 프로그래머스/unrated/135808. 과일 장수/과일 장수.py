def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True) # 내림차순 정렬
        
    for i in range(0, len(score), m):
        # 0부터 len(score)-1까지 m개씩 자름
        current_box = score[i:i+m]
        if len(current_box) == m:
            answer += min(current_box) * m

    return answer