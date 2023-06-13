import copy

def solution(plans):
    answer = []
    
    stop = []
    plans = sorted(plans, key = lambda x: x[1]) # sort plans by start time
    for i in range(len(plans)):
        if i != len(plans)-1: # if this is not the last plan
            # endtime of current plan
            temp = int(plans[i][1][0:2])*60 + int(plans[i][1][3:]) + int(plans[i][2]) 
            
            # starttime of the next plan
            next = int(plans[i+1][1][0:2])*60 + int(plans[i+1][1][3:])
            
            if temp <= next:
                # if the current plan ends before next plan starts
                answer.append(plans[i][0])
                if len(stop)>0: # if paused plan exists
                    lis = copy.deepcopy(stop)
                    tp = next-temp # paused plan 끝내려면 남은 시간
                    for j in range(len(stop)-1, -1, -1):
                        # 제일 최근에 pause된 plan부터 고려
                        if stop[j][1] <= tp:
                            # 다음 과제 시작 전에 지금 pause되어 있는 과제가 완료된다면
                            tp -= stop[j][1]
                            answer.append(stop[j][0])
                            lis.pop()
                        else:
                            lis[-1][1] = stop [j][1] - tp
                            # 지금 pause되어 있는 과제 완료에 필요한 시간에서 (다음 과제 시작 시간 - 현재 시간)을 뺌
                            break
                    stop = copy.deepcopy(lis)
            else: # temp > next (다음 과제 시작 전까지 현재 과제가 안 끝남)
                stop.append([plans[i][0], temp-next])
        else:
            answer.append(plans[i][0]) # if i == len(plans)-1 # 현재 과제가 마지막 과제라면
    
    for i in range(len(stop)-1, -1, -1):
        answer.append(stop[i][0])    # 제일 최근에 pause된 과제부터 순서대로 완료 후 answer list에 과제 이름 추가        
    
    return answer