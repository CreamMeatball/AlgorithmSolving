import sys

N, K = map(int, sys.stdin.readline().split())

circle = [(i+1) for i in range(N)]

result = []

i = 0

while(len(circle) > 0):
    i = (i + K - 1) % len(circle)
    # print("i : ", i)
    result.append(circle.pop(i))
    # print("circle : ", circle)

print("<", end="")

for i in result:
    print(i, end=", ") if i != result[-1] else print(i, end="")
    
print(">")