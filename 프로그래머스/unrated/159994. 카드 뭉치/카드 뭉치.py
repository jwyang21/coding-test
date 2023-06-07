def solution(cards1, cards2, goal):
    pnt1 = 0
    pnt2 = 0
    num_words = 0

    for i in range(len(goal)):
        target = goal[i]
        #print(f'\n===target: {target}')
        if pnt1 < len(cards1) and cards1[pnt1]==target:
            #print(f'Top word from cards1: ', cards1[pnt1])
            num_words += 1
            pnt1 += 1
        elif pnt2 < len(cards2) and cards2[pnt2]==target:
            #print(f'Top word from cards2: ', cards2[pnt2])
            num_words += 1
            pnt2 += 1
        else:
            break
    if num_words == len(goal):
        result = "Yes"
    else:
        result = "No"
    return result