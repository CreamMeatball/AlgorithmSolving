import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())
road = list(map(int, input_data().split()))
city = list(map(int, input_data().split()))

min_cost = city[0]
cost = 0

for i in range(N-1):
    if city[i] < min_cost:
        min_cost = city[i]
    cost += min_cost * road[i]
    
print(cost)