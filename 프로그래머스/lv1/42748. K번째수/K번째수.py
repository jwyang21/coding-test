def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tmp = commands[i]
        sublist = sorted(array[tmp[0]-1:tmp[1]]) # sorted([array[i], ..., array[j]])
        answer.append(sublist[tmp[2]-1])
    return answer