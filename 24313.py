a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

result = 1

for i in range(n0, 101):
    f_i = i * a1 + a0
    if f_i > c * i:
        result = 0
        break
    
print(result)