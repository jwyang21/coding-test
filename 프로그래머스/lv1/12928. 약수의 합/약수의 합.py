def divisor(n):
    answer = []
    for i in range(1, int(n ** (1/2))+1):
        if n % i == 0:
            answer.append(i)
            if i ** 2 != n:
                answer.append(n//i)
    return answer

def solution(n):
    divisor_list = divisor(n)
    return sum(divisor_list)