n = int(input())

# 1 + 2 + 3 + ... + (n - 4) + (n - 3) + (n - 2)
# 1 + 2 + 3 + ... + (n - 4) + (n - 3)
# 1 + 2 + 3 + ... + (n - 4)
# ...
# 1 + 2 + 3
# 1 + 2
# 1

sum = 0
for i in range(n - 2):
    k = n - 2 - i
    sum += (k + 1) * k // 2
    
print(sum)
print(3)