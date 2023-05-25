def solution(new_id):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']
    
    #1
    tmp = new_id.lower()
    
    #2
    for i in list(set(tmp)):
        if i not in chars:
            tmp = tmp.replace(i, '')
            
    #3
    while '..' in tmp:
        tmp = tmp.replace('..', '.')

    #4
    if tmp[0] == '.':
        tmp = tmp[1:]
    if len(tmp) >= 1:
        if tmp[-1] == '.':
            tmp = tmp[:-1]
        
    #5
    if len(tmp) == 0:
        tmp += 'a'
        
    #6
    if len(tmp) >= 16:
        tmp = tmp[:15]
    if tmp[-1] == '.':
        tmp = tmp[:-1]
        
    #7
    if len(tmp) <= 2:
        while len(tmp) < 3:
            tmp = tmp + tmp[-1]
    
    return tmp