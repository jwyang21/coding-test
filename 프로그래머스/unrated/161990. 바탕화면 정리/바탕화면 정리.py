def solution(wallpaper):
    row_indices = []
    column_indices = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                row_indices.append(i)
                column_indices.append(j)
    #print('row_indices: ', row_indices)
    #print('column_indices: ', column_indices)
    result = [min(row_indices), min(column_indices), max(row_indices)+1, max(column_indices)+1]
    #print('result: ', result)
    return result