def solution(d, budget):
    if sum(d) <= budget:
        answer = len(d)
    
    else:
        if len(d) == 1 and d[0] > budget:
            answer = 0
        else:
            max_ = -999
            d = sorted(d)
            window_size = len(d)-1
            answer_flag = 0
            while window_size >= 1 and answer_flag == 0:
                for i in range(len(d)-window_size+1):
                    #print(i)
                    tmp = d[i:i+window_size]
                    if sum(tmp) <= budget and len(tmp) > max_:
                        max_ = len(tmp)                  
                        #print(f'answer: {max_} (sum of {tmp} <= budget {budget})')
                        answer_flag += 1                
                window_size -= 1
            answer = max_
    return answer