def solution(numbers):
    answer = sum(list(set(list(range(0, 10))) - set(numbers)))
    return answer