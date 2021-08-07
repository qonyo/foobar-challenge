from itertools import combinations
from collections import Counter

def solution(l):
    if len(l) <= 2:
        return 0
    
    div_check = list(set(comb for comb in combinations(l,2)))
    unique_count = dict(Counter(l))
    divisors_count = dict.fromkeys(unique_count.keys(), 0)
    multipliers_count =  dict.fromkeys(unique_count.keys(), 0)
    triples_total = 0
    for check in div_check:
        if check[0] % check[1] == 0:
            divisors_count[check[0]] += 1
            multipliers_count[check[1]] += 1
        elif check[1] % check[0] == 0:
            divisors_count[check[1]] += 1
            multipliers_count[check[0]] += 1
    
    for member in unique_count:
        if unique_count[member] == 2:
            triples_total += ((divisors_count[member]*multipliers_count[member]) - 1)
            continue
        triples_total += (divisors_count[member]*multipliers_count[member])
    return triples_total
    
print(solution([1,1,1]))