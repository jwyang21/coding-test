def solution(s):
    if len(s) not in [4, 6]:
        return False
    for i in range(len(s)):
        ord_ = ord(s[i])
        if ord_ < 48 or ord_ > 57:
            return False
    return True