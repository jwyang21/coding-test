def count_num_divisor(n: int) -> int :
    answer = 0
    #print(int(n**(1/2)))
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer += 1
            #print(i, n // i)
            if i ** 2 != n:
                answer += 1
    return answer

def solution(left, right):
    answer = 0
    
    num_divisor = {}
    for i in range(left, right+1):
        num_divisor[str(i)] = count_num_divisor(i)
        
    for i in range(len(list(num_divisor.keys()))):
        k, v = list(num_divisor.keys())[i], list(num_divisor.values())[i]
        if v % 2 == 0:
            answer += int(k)
        else:
            answer -= int(k)
    return answer