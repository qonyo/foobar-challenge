def solution(n):
    count = 0
    while n != 1:
        if n%2==0:
            n /= 2
        elif n%8 == 7:
            n += 1
        else:
            n-=1
        count += 1
    return count

print(solution(4))
print(solution(15))