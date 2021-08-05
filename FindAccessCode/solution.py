def factorial(n):
    if n<2:
        return 1
    else :
        return n*factorial(n-1)

def combination(item, take):
    combination = factorial(item)/(take*factorial(item-take))
    return int(combination)

def solution(l):
    l = [1,2,3,4,5,6]
    test2 = [1,1,1]
    count = 0
    divisible = [0]*len(l)
    
    for index_divisor, divisor in enumerate(l):
        for index_dividend, dividend in enumerate(l[index_divisor:]):
            if dividend%divisor == 0:
                divisible[index_dividend] += 1
        
    for div_num in divisible:
        if div_num < 2:
            continue
        else:
            count += combination(div_num, 2)
    return count  
    
print(solution(0))