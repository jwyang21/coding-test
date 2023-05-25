def count_divisor(n):
    answer = 0
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            answer += 1
            if i ** 2 != n:
                answer += 1
    return answer

def solution(number, limit, power):
    power_list = []

    for i in range(number):
        power_list.append(count_divisor(i+1))
        
    for i in range(len(power_list)):
        current_power = power_list[i]
        if current_power > limit:
            power_list[i] = power
            
    return sum(power_list)