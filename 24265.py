n = int(input())

# (n - 1) + (n - 2) + ... + 1
# = ((n - 1) + 1) * (n - 1) / 2
iternum = n * (n - 1) // 2
print(iternum)
print(2)