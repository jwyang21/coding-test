def solution(name, yearning, photo):
    answer = []
    for p in photo:
        current_photo_score = 0
        for n in p:
            if n in name:
                name_index = name.index(n)
                name_score = yearning[name_index]
                current_photo_score += name_score
        answer.append(current_photo_score)
    return answer