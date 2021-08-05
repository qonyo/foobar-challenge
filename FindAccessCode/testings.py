def factorial(n):
    if n<2:
        return 1
    else :
        return n*factorial(n-1)

def combination(item, take):
    combination = factorial(item)/(take*factorial(item-take))
    return combination
    
print(combination(10,2))