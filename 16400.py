# PyPy3 avoiding time exceed

N = int(input())

DIVISOR = 123456789

dp = [0] * (N + 1)
dp[0] = 1

# 에라토스테네스의 체 (prime 리스트 다 구할 때는 이게 효율적)
primes = []
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
            
for i in range(2, N + 1):
    if is_prime[i]:
        primes.append(i)

# print(primes)

for p in primes:
    # 동전을 무한히 쓸 수 있으므로 앞에서 뒤로 갱신
    # (한 번씩밖에 못 쓰는 거면, 뒤에서 앞으로 갱신하는 게 효율적)
    for i in range(p, N + 1):
        dp[i] = (dp[i] + dp[i - p]) % DIVISOR

# print(dp)

print(dp[N])