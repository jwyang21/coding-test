def solution(s, n):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters += letters.lower()
    
    tmp = ''
    for i in range(len(s)):
        if s[i] == ' ':
            tmp += ' '
        else:
            ind = letters.index(s[i])
            ind += n
            if s[i] == s[i].upper():
                if ind >=26:
                    ind -= 26
            else:
                if ind >= len(letters):
                    ind -= 26
            tmp += letters[ind]
            
    return tmp