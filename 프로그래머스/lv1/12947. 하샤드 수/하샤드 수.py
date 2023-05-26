def solution(x):
    sum_digits = 0
    initial_x = x
    while x > 0:
        sum_digits += x%10
        x = x//10
    answer = (initial_x%sum_digits)==0
    return answer