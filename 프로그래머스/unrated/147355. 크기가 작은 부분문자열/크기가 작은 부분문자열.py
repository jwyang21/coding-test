def solution(t, p):
    window_size = len(p)
    answer = 0
    for i in range(len(t)-window_size+1):
        probe = int(t[i:i+window_size])
        #print(probe)
        if probe <= int(p):

            answer += 1
    return answer