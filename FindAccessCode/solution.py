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
print(solution([1,1,1]))