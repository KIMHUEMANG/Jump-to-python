import math

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        weapon_power = get_divisors(i)
        if weapon_power > limit:
            weapon_power = power
        answer += weapon_power

    return answer

def get_divisors(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    if n > 1:
        divisors.append(n)
    return len(divisors)