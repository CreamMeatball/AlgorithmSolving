import sys

input_data = sys.stdin.readline

N = int(input_data())

left = 0
right = 0
huddle = 0

trophy = []
for _ in range(N):
    t = int(input_data())
    trophy.append(t)
    if t > huddle:
        left += 1
        huddle = t

huddle = 0

for i in range(N-1, -1, -1):
    if trophy[i] > huddle:
        right += 1
        huddle = trophy[i]
        
print(left)
print(right)
