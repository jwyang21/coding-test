def solution(s):
    indices = {}
    answer = []
    for i in range(len(s)):
        x = s[i]
        #print("---")
        #print(f'{i}th character: {x}')
        #print(indices)     
        if x in list(indices.keys()):
            #print('add {}'.format(indices[x]))
            answer.append(i-indices[x])
        else:
            answer.append(-1)
            #print('add -1')
        indices[x] = i
    return answer