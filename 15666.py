# from itertools import product
from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# products = set()

# for prod in product(numbers, repeat = M):
#     products.add(prod)
    
# products = sorted(products) 
    
# print(*products)
    
# for p in products:
#     print(*p)

combs = set()
for comb in combinations_with_replacement(numbers, M):
    comb = sorted(comb) # tuple -> sorted list
    combs.add(tuple(comb))
    
combs = sorted(combs)

for c in combs:
    print(*c)