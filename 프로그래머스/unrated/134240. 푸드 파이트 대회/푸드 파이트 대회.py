def solution(food):
    tmp = ''
    for i in range(1, len(food)):
        current_food = str(i)
        tmp += str(i) * (food[i]//2)
    answer = tmp + '0' + tmp[::-1]
    return answer