def factorial(n):
    if n<2:
        return 1
    else :
        return n*factorial(n-1)

def combination(item, take):
    combination = factorial(item)/(take*factorial(item-take))
    return int(combination)

def solution(l):
    if len(l) <= 2:
        return 0
    
    
print(solution(0))