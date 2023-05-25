def solution(s):
    d = {}
    d['zero'] = 0
    d['one'] = 1
    d['two'] = 2
    d['three'] = 3
    d['four'] = 4
    d['five'] = 5
    d['six'] = 6
    d['seven'] = 7
    d['eight'] = 8
    d['nine'] = 9
    
    for character in list(d.keys()):
        if character in s:
            s = s.replace(character, str(d[character]))
    
    answer = int(s)
    
    return answer