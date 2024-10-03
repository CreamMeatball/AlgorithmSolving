factors = []

while(True):
    N = int(input())
    if N == -1:
        break
    for i in range(1, N):
        if N % i == 0:
            factors.append(i)
    if sum(factors) == N:
        print(f"{N} = {' + '.join(str(f) for f in factors)}")
    else:
        print(f"{N} is NOT perfect.")
    factors = []