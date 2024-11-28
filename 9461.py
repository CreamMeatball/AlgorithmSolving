# 1 : 고정
# 1 : n-1
# 1 : n-1
# 2 : n-1 + n-3(=n-2)
# 2 : n-1
# 3 : n-1 + n-3
# 4 : n-1 + n-6
# 5 : n-1 + n-7
# 7 : n-1 + n-5
# 9 : n-1 + n-5
# 12 : n-1 + n-5
# 16 : n-1 + n-5
# 21 : n-1 + n-5

numbers = [0 for _ in range(101)]
numbers[1] = 1
numbers[2] = 1
numbers[3] = 1
numbers[4] = 2
numbers[5] = 2
numbers[6] = 3
numbers[7] = 4
numbers[8] = 5

calculated = 8

def dp(n):
    global calculated
    if n < 8:
        return numbers[n]
    elif n > calculated:
        for i in range(calculated+1, n+1):
            numbers[i] = numbers[i-1] + numbers[i-5]
        calculated = n
        return numbers[n]
    else:
        return numbers[n]

T = int(input())
for i in range(T):
    N = int(input())
    print(dp(N))