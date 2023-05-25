def solution(numbers, hand):
    numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']

    coords = []
    for i in range(4):
        for j in range(3):
            coords.append([i, j])
    
    d = dict(zip(numbers_, coords))
    
    left_keys = [1, 4, 7]
    right_keys = [3, 6, 9]
    
    left_num = '*'
    right_num = '#'
    
    result = ''
    
    for i in range(len(numbers)):
        current = numbers[i]
        if current in right_keys:
            right_num = current
            result += 'R'
        elif current in left_keys:
            left_num = current
            result += 'L'
        else:
            left_distance = abs(d[left_num][0] - d[current][0]) + abs(d[left_num][1] - d[current][1])
            right_distance = abs(d[right_num][0] - d[current][0]) + abs(d[right_num][1] - d[current][1])
            if left_distance < right_distance:
                left_num = current
                result += 'L'
            elif right_distance < left_distance:
                right_num = current
                result += 'R'
            else:
                if hand == 'left':
                    left_num = current
                    result += 'L'
                else:
                    right_num = current
                    result += 'R'

    return result