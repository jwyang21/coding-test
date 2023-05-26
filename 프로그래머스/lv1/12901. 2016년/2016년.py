def solution(a, b):
    month_31_days = [1, 3, 5, 7, 8, 10, 12]
    month_30_days = [4, 6, 9, 11]
    
    days_name = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    num_days = 0
    for i in range(1, a):
        if i in month_31_days:
            num_days += 31
        elif i in month_30_days:
            num_days += 30
        else:
            num_days += 29
    num_days += (b-1)
    
    answer = days_name[num_days % len(days_name)]
    
    return answer