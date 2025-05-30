import sys
from itertools import permutations

input_ = sys.stdin.readline

N = int(input_().rstrip())

tips = list(int(input_().rstrip()) for _ in range(N))

# 결국 순서가 어떻게 되든간에
# 순서로 인한 마이너스의 총합은 똑같음
# N = 3 이면 마이너스의 총합이 6임.
# 근데 이제 결과가 달라지는 이유가
# tip - i 해서 음수가 되면 0원으로 되기 때문.

# 그러면 tip 금액이 적은 데다가 큰 값의 i 를 마이너스 시켜서 버리는 게 무조건 이득
# 5 - 100 이든 99 - 100 이든 똑같이 0원이기 때문에.

# 결국 Greedy 하게, tip 많이 줄 순서대로(내림차순) 정렬하면 그게 최대값일 듯.

tips.sort(reverse=True)

result = 0
for i in range(N):
    total = tips[i] - i
    total = max(0, total)
    result += total
    
print(result)