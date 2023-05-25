def solution(id_list, report, k):
    report = list(set(report))
    report_inverse_d = {} # key: reportee # value: reporter
    
    report_count = {}
    for id_ in id_list:
        report_count[id_] = 0

    mail_count = {}
    for id_ in id_list:
        mail_count[id_] = 0
        
    for x in report:
        reporter, reportee = x.split(' ')
        report_count[reportee] += 1
        if reportee not in list(report_inverse_d.keys()):
            report_inverse_d[reportee] = [reporter]
        else:
            report_inverse_d[reportee].append(reporter)
            
    for id_ in list(report_count.keys()):
        if report_count[id_] >= k:
            for reporter in report_inverse_d[id_]:
                mail_count[reporter] += 1
    
    answer = [x for x in list(mail_count.values())]
    
    return answer