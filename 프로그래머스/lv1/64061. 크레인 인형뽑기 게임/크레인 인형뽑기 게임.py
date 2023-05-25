import numpy as np

def solution(board, moves):
    board = np.array(board)
    draws = []
    pop = 0
    for move in moves:
        count = 0
        #print(f"===\nmove: {move}")
        column = board[:, move-1]
        if list(column).count(0) == len(column):
            #print('Current column is filled with 0')
            pass
        else:
            for i in range(len(column)):            
                if column[i] != 0:
                    if count == 0:
                        #print("Doll {}".format(column[i]))
                        if len(draws)>0:
                            if draws[-1] == column[i]:
                                pop += 1                            
                                count += 1
                                #print("Pop: last doll {} = current draw {}".format(draws[-1], column[i]))
                                draws = draws[:-1]
                                board[i][move-1] = 0
                            else:
                                draws.append(column[i])   
                                #print(f'Append doll to draws: {draws}')
                                count += 1
                                board[i][move-1] = 0
                        else:
                            draws.append(column[i])
                            #print(f'Append doll to draws: {draws}')
                            count += 1
                            board[i][move-1] = 0
                    else:
                        pass
                        #print(f'count is nonzero: {count}')
        #print('board')
        #print(board)
    return pop*2