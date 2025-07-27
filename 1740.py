N = int(input())
answer = 0
p3 = 1
while N > 0:
    if N & 1:
        answer += p3
    p3 *= 3
    N >>= 1
print(answer)
