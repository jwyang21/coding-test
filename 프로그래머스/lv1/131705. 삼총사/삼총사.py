def solution(number):
    answer = 0
    for i in range(len(number)):
        first = number[i]
        for j in range(i+1, len(number)):
            second = number[j]
            for k in range(j+1, len(number)):
                if number[k] == (-1) * (first+second):
                    answer += 1
    return answer