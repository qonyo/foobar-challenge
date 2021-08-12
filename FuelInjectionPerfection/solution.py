def solution(n):
    if n==1:
        return 0
    elif n%2 ==0:
        return 1+solution(n/2)
    elif n%8 == 7:
        return 1+solution(n+1)
    else:
        return 1+solution(n-1)

print(solution(4))
print(solution(15))