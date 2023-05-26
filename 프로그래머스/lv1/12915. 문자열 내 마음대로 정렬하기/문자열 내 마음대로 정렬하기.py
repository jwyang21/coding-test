def solution(strings, n):
    target_ords = []
    for x in strings:
        target_ords.append(ord(x[n]))
        
    dct = {}
    for i in range(len(target_ords)):
        if target_ords[i] in list(dct.keys()):
            dct[target_ords[i]].append(strings[i])
        else:
            dct[target_ords[i]] = [strings[i]]
            
    sorted_dct = sorted(dct.items(), key = lambda x: x[0])
    
    answer = []
    for i in range(len(sorted_dct)):
        #print(f'i: {i}')
        #print(sorted_dct[i][1])
        if len(sorted_dct[i][1])==1:
            #print("Length 1")
            answer.append(sorted_dct[i][1][0])
        else:
            tmp = sorted_dct[i][1].copy()
            #print(tmp)
            tmp.sort()
            #print(tmp)
            for x in tmp:
                answer.append(x)
    return answer