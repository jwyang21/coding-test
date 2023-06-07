def solution(s, skip, index):
    alphabet =  "abcdefghijklmnopqrstuvwxyz" 

    for skip_chr in skip:
        if skip_chr in alphabet:
            alphabet = alphabet.replace(skip_chr, '')

    answer = ''
    for i in range(len(s)):
        new = (alphabet.index(s[i])+index)%len(alphabet)
        answer += alphabet[new]
    return answer