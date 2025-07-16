import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
city = []
house_pos = []
chicken_pos = []
for i in range(N):
    data = list(map(int, input().rstrip().split()))
    for j, d in enumerate(data):
        if d == 1:
            house_pos.append((i, j))
        elif d == 2:
            chicken_pos.append((i, j))
    city.append(data)
    
# print("houses")
# for h in house_pos:
#     print(h)
    
# print("chickens")
# for c in chicken_pos:
#     print(c)
    
min_city_chicken_dist = float('inf')

def calculate_dist(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

survived_chicken_pos_comb = combinations(chicken_pos, M)

for survived_chickens in survived_chicken_pos_comb:
    # print(f"for this chickens comb: {survived_chickens}")
    current_city_chicken_dist = 0
    for house in house_pos:
        current_house_chicken_dist = float('inf')
        for survived_chicken in survived_chickens:
            current_house_chicken_dist = min(current_house_chicken_dist, calculate_dist(house, survived_chicken))
        current_city_chicken_dist += current_house_chicken_dist
    # print(f"current_city_chicken_dist: {current_city_chicken_dist}")
    min_city_chicken_dist = min(min_city_chicken_dist, current_city_chicken_dist)
    
print(min_city_chicken_dist)