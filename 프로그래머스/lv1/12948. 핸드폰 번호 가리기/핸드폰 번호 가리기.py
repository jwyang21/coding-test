def solution(phone_number):
    last_four_digits = phone_number[-4:]
    tmp = '*'*(len(phone_number) - 4)
    tmp += last_four_digits
    return tmp