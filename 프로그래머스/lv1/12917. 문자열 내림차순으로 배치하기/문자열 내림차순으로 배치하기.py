def solution(s):
    ord_list = []
    for i in range(len(s)):
        ord_list.append(ord(s[i]))
    ord_list.sort(reverse=True)
    answer = ''
    for i in range(len(ord_list)):
        answer += chr(ord_list[i])
    return answer