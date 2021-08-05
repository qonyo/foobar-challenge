def factorial(n):
    if n<2:
        return 1
    else :
        return n*factorial(n-1)

def combination(item, take):
    combination = factorial(item)/(take*factorial(item-take))
    return int(combination)

def solution(l):
    l = [1,2,2,4]
    count = 0
    divisible = [0]*len(l)
    for index_divisor, divisor in enumerate(l):
        for index_dividend, dividend in enumerate(l[index_divisor+1:]):
            if dividend%divisor == 0:
                divisible[index_dividend + index_divisor +1] += 1  
    for div_num in divisible:
        if div_num < 2:
            continue
        else:
            count += div_num -1
    return count
print(solution(0))