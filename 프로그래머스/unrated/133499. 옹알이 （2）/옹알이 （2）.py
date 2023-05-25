def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    count = 0
    for babble in babbling:
        #print(f'===\n{babble}')
        for word in words:
            #print(f'---\n{word}')
            if word*2 not in babble:
                babble = babble.replace(word, ' ')
                #print('replace')
        if babble.strip() == '':
            count += 1
    return count