def solution(survey, choices):
    keylist = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    category = ['RT', 'CF', 'JM', 'AN']
    
    score = {}
    for k in keylist:
        score[k] = 0
    
    answer = ''
    
    for i in range(len(survey)):
        type_ = survey[i]
        answer = choices[i]-4
        if answer < 0:
            score[type_[0]] += abs(answer)
        elif answer > 0:
            score[type_[1]] += answer
        else:
            pass
        
    answer = ''
    for c in category:
        score_1 = score[c[0]]
        score_2 = score[c[1]]
        if score_2 > score_1:
            answer += c[1]
        elif score_1 > score_2:
            answer += c[0]
        else:
            if ord(c[0]) < ord(c[1]):
                answer += c[0]
            else:
                answer += c[1]
    return answer