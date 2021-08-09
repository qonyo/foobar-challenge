from itertools import combinations
from collections import Counter

def solution(l):
    unique_count = Counter(l)
    divisors_count = Counter()
    multipliers_count =  Counter()
    triples_total = 0
    for x,y in combinations(sorted(unique_count),2):
        if y % x == 0:
            divisors_count[y] += 1
            multipliers_count[x] += 1
    for x,n in unique_count.items():
        triples_total += divisors_count[x]*multipliers_count[x]
        if n >= 2:
            triples_total += divisors_count[x] + multipliers_count[x]
            if unique_count[x] >=3 :
                triples_total += 1
    return triples_total
print(solution([1,2,2,2,3,3,3,4,4,4,5,5,6]))

def solutionz(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        j=0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count
print(solutionz([1,2,2,2,3,3,3,4,4,4,5,5,6]))