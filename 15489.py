R, C, W = map(int, input().split())

len_ = (R + W - 1) * (R + W - 1 + 1) // 2 + 1 # whole dp len

dp = [0] * (len_)
dp[1] = 1

# 어느 (r, c) 위치의 순차적 index가 몇?: (1 <= r, 1 <= c)
# (r - 1) * (r) // 2 + c

def cal_pos(r, c):
    return (r - 1) * r // 2 + c

for r in range(1, R + W - 1 + 1):
    for c in range(1, r + 1):
        pos = cal_pos(r, c)
        # print(f"r: {r}, c: {c}, pos: {pos}")
        if (c == 1) or (c == r):
            dp[pos] = 1
        else:
            prev_pos1 = cal_pos(r - 1, c - 1)
            prev_pos2 = cal_pos(r - 1, c)
            dp[pos] = dp[prev_pos1] + dp[prev_pos2]
            
# print(dp)

result = 0

result_loop_len = W * (W + 1) // 2

start_r = R
start_c = C

for i in range(1, W + 1):
    # print(i)
    for j in range(1, i + 1):
        pos = cal_pos(start_r - 1 + i, start_c - 1 + j)
        # print(f"r: {start_r - 1 + i}, c: {start_c - 1 + j}, pos: {pos}, -> dp[pos]: {dp[pos]}")
        result += dp[pos]
        
print(result)