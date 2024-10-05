def is_prime(number):
    if number == 1:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1

primelist = []

M = int(input())
N = int(input())

min = None

for n in range(M, N+1):
    is_prime_value = is_prime(n)
    (primelist.append(n)) if is_prime_value else None
    min = n if (is_prime_value and (min is None or n < min)) else min
    
# print(primelist)
print(f"{sum(primelist)}\n{min}") if len(primelist) else print(-1)