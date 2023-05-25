def solution(ingredient):
    tmp = []
    answer = 0
    for i in range(len(ingredient)):
        tmp.append(ingredient[i])
        if tmp[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                tmp.pop()
    return answer