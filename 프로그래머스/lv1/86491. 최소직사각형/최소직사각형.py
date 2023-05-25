def solution(sizes):
    w_list = []
    h_list = []

    for i in range(len(sizes)):
        w, h = sizes[i][0], sizes[i][1]
        if w >= h:
            w_list.append(w)
            h_list.append(h)
        else:
            w_list.append(h)
            h_list.append(w)
    answer = max(w_list) * max(h_list)
    
    return answer