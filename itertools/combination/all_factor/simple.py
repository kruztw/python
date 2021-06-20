from itertools import combinations

factors = [1]
prime_factors = [2, 2, 3, 5]

for i in range(1, len(prime_factors)+1):
    for n in list(combinations(prime_factors, i)):
        factor = 1
        for i in n:
            factor *= i
        factors.append(factor)

print(sorted(set(factors)))
