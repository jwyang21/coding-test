def solution(n, arr1, arr2):
    map1 = []
    for i in range(n):
        map1_coded = arr1[i]
        map1_coded = bin(map1_coded).replace('0b', '')
        if len(map1_coded) < n:
            while len(map1_coded) < n:
                map1_coded = '0' + map1_coded
        map1.append(map1_coded)
        
    map2 = []
    for i in range(n):
        map2_coded = arr2[i]
        map2_coded = bin(map2_coded).replace('0b', '')
        if len(map2_coded) < n:
            while len(map2_coded) < n:
                map2_coded = '0' + map2_coded
        map2.append(map2_coded)
        
    answer = []
    for i in range(n):
        tmp = ''
        for j in range(len(map1[i])):
            if int(map1[i][j]) + int(map2[i][j]) == 0:
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
    return answer