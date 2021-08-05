def factorial(n):
    if n<2:
        return 1
    else :
        return n*factorial(n-1)

def combination(item, take):
    combination = factorial(item)/(take*factorial(item-take))
    return combination
    
a = [3,2,1]
a.sort()
print(a)