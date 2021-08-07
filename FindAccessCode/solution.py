from itertools import combinations
from collections import Counter

def solution(l):
    if len(l) <= 2:
        return 0
    
    div_check = list(set(comb for comb in combinations(sorted(l),2)))
    unique_count = dict(Counter(l))
    divisors_count = dict.fromkeys(unique_count.keys(), 0)
    multipliers_count =  dict.fromkeys(unique_count.keys(), 0)
    triples_total = 0
    for x,y in div_check:
        if y % x == 0:
            divisors_count[y] += 1
            multipliers_count[x] += 1
    
    for member in unique_count:
        if unique_count[member] == 2:
            triples_total += ((divisors_count[member]*multipliers_count[member]) - 1)
            continue
        triples_total += (divisors_count[member]*multipliers_count[member])
    return triples_total
    
print(solution([8,2,4,2,4]))