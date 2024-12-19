N, K = map(int, input().split())
temperature = list(map(int, input().split()))

accum_sum = [sum(temperature[:K])]

for i in range(K, N):
    accum_sum.append(accum_sum[-1] - temperature[i-K] + temperature[i])
    
print(max(accum_sum))