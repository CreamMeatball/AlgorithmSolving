import sys

input = sys.stdin.readline

n = int(input().split()[0])
total_sum = 0
results = []

# 카데인 알고리즘
# 배열에서 연속된 부분 배열의 합이 최대가 되는 구간을 단 한 번의 순회($O(n)$)로 찾아내는 동적 계획법(DP) 알고리즘.
# $$dp[i] = \max(A[i], dp[i-1] + A[i])$$

# 행 별로 독립적으로 best 탐색

for _ in range(n):
    l = int(input().split()[0])
    gems = []
    while len(gems) < l:
        gems.extend(map(int, input().split()))
    
    best_row = (-float('inf'), -float('inf'), -float('inf'), -float('inf'))
    curr_sum, curr_len, curr_start = -float('inf'), 0, 0
    
    for i in range(1, l + 1):
        val = gems[i-1]
        
        if (val, -1, -i) >= (curr_sum + val, -(curr_len + 1), -curr_start):
            curr_sum, curr_len, curr_start = val, 1, i
        else:
            curr_sum, curr_len = curr_sum + val, curr_len + 1
            
        cand = (curr_sum, -curr_len, -curr_start, -i)
        if cand > best_row:
            best_row = cand
            
    total_sum += best_row[0]
    results.append((-best_row[2], -best_row[3]))

print(total_sum)
for r in results:
    print(f"{r[0]} {r[1]}")
