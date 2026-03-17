import sys
from bisect import bisect_left

# 결국 LIS 알고리즘임 (가장 긴 증가하는 부분수열(연속하지 않아도 됨))
# 방어력보다 높은 대미지로만 연속해서 계속 쏘고
# 중간에 허공으로 쏠 수 있으니
# LIS 구하기랑 같음

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def get_max_hits(bullets):
    max_score = 0
    double_bullets = bullets + bullets
    for i in range(N):
        current_sequence = double_bullets[i:i+N]
        dp = []
        for power in current_sequence:
            pos = bisect_left(dp, power)
            if pos == len(dp):
                dp.append(power)
            else:
                dp[pos] = power
        if len(dp) > max_score:
            max_score = len(dp)
    return max_score

yj_score = get_max_hits(A)
hg_score = get_max_hits(B)

if yj_score > hg_score:
    print("YJ Win!")
elif hg_score > yj_score:
    print("HG Win!")
else:
    print("Both Win!")
