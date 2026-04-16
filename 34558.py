import sys

input = sys.stdin.readline

N = int(input().rstrip())
max_len = 1000000

ab = []
for _ in range(N):
    ab.append(list(map(int, input().split())))
    
def eratos(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    prefix_sum = [0] * (max_n + 1)
    primes = []
    for i in range(1, max_n + 1):
        if is_prime[i]:
            primes.append(i)
        prefix_sum[i] = prefix_sum[i-1] + (1 if is_prime[i] else 0)
    
    return prefix_sum, primes

prefix_sum, primes = eratos(max_len)

result = []
for a, b in ab:
    count = prefix_sum[b] - prefix_sum[a - 1]
    if (count == 0) or (count % 2 == 0):
        result.append(-1)
    else:
        rank = prefix_sum[a - 1] + (count // 2) + 1
        result.append(primes[rank - 1])
        
print('\n'.join(map(str, result)))