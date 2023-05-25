def solution(today, terms, privacies):
    term = {}
    for t in terms:
        key, value = t.split(' ')
        value = int(value)
        term[key] = value
        
    year2month = 12
    month2day = 28
        
    current_year, current_month, current_day = today.split('.')
    current_year, current_month, current_day = int(current_year), int(current_month), int(current_day)
    current_date = current_year * year2month * month2day + current_month * month2day + current_day
    
    answer = []    
    for i in range(len(privacies)):
        p = privacies[i]
        s, t = p.split(' ')
        duration = term[t]
        start_year, start_month, start_day = s.split('.')
        start_year, start_month, start_day = int(start_year), int(start_month), int(start_day)
        end_year, end_month, end_day = start_year, start_month + duration, start_day
        end_date = end_year * year2month * month2day + end_month * month2day + end_day - 1
        if end_date < current_date:
            answer.append(i+1)
    return answer