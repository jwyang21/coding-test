def solution(x, n):
    answer = []
    initial_x = x
    while len(answer) < n:
        answer.append(x)
        x += initial_x
    return answer