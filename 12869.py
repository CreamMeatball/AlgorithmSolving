N = int(input())
scvs = list(map(int, input().split()))

# 횟수를 DP의 값으로 해야함
dp = [[[0] * (scvs[0] + 1) for _ in range(scvs[1] + 1)] for _ in range(scvs[2] + 1)]
# dp[i][j][k]: 각 scv의 hp가 hp1, hp2, hp3 일 때 모든 scv를 파괴하기 위한 최소 공격 횟수

destroy_count = 0

attack_case = [(9,3,1), (9,1,3), (3,9,1), (3,1,9), (1,9,3), (1,3,9)]

for i in range(1, scvs[0] + 1):
    for j in range(1, scvs[1] + 1):
        for k in range(1, scvs[2] + 1):
            None