def solution(s):
    tmp = ''
    index = 0
    for i in range(len(s)):
        if s[i] == ' ':
            index = 0
            tmp += ' '
        else:
            if index % 2 == 0:
                tmp += s[i].upper()
                index += 1
            else:
                tmp += s[i].lower()
                index += 1
    return tmp