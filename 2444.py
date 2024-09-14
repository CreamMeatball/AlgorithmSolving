N = int(input())

for i in range(0, N):
    print(" " * (N-1-i) + "*" * (1+2*i))
for i in range(N-1, 0, -1):
    print(" " * (N-i) + "*" * (2*i-1))
    
# 별 뒤에 띄어쓰기 더 붙이면 안됨