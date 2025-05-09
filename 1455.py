import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().rstrip().split())

coins = []
for _ in range(N):
    coins.append(list(map(int, str(input_data().rstrip()))))
    
# print(coins)
    
def flip(coins, a, b):
    for i in range(a + 1):
        for j in range(b + 1):
            coins[i][j] = 1 - coins[i][j]
            
count = 0

# greedy
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if coins[i][j] == 1:
            count += 1
            flip(coins, i, j)

print(count)