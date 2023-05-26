import numpy as np

def divisor(x):
    answer = []
    for i in range(1, int(x**(1/2))+1):
        if x % i == 0:
            answer.append(i)
            if i ** 2 != x:
                answer.append(x//i)
    return sorted(answer)

def gcd(x, y):
    x_divisor = divisor(x)
    y_divisor = divisor(y)
    cd = np.intersect1d(x_divisor, y_divisor).tolist()
    return max(cd)

def lcm(x, y):
    for i in range(max(x,y), x*y+1):
        if i % x == 0 and i % y == 0:
            return i

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer