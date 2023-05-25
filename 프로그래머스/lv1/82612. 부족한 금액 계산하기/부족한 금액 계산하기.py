def solution(price, money, count):
    total_price = 0
    for i in range(count):
        total_price += price * (i+1)
        
    if total_price >= money:
        answer = total_price - money
    else:
        answer = 0

    return answer