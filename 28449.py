import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 그냥 계산하면 O(N*M) 이니까
# 실력 x일 때 '몇 명'이나 이기는지를 누적합으로 미리 구해놓자, 라는 아이디어.

MAX_SKILL = 100000

freq_a = [0] * (MAX_SKILL + 1) # freq_a[s]: HI팀에서 실력 s인 사람 수
freq_b = [0] * (MAX_SKILL + 1)

for x in a:
	freq_a[x] += 1

for x in b:
	freq_b[x] += 1

pref_b = [0] * (MAX_SKILL + 1)
for s in range(1, MAX_SKILL + 1):
	pref_b[s] = pref_b[s - 1] + freq_b[s]

hi_win = 0
arc_win = 0
draw = 0

# 근데 반복문 도는 것도 HI팀, ARC팀 따로 도는 게 아니라
# 한 번에 돌면서 계산.
# 왜냐면 binary 승부니까
# 한 쪽 팀 입장에서 승/무/패 정하면, 다른쪽팀은 동일한 수만큼 반대로 됨.

for s in range(1, MAX_SKILL + 1): # HI 입장에서, 실력 s 기준으로 루프 돌기
	cnt = freq_a[s]
	if cnt == 0:
		continue
	lower = pref_b[s - 1] # HI 의 실력 s 보다 낮은 ARC 명 수
	equal = freq_b[s] # HI 의 실력 s 랑 동일한 ARC 명 수
	higher = M - pref_b[s] # HI 의 실력 s 보다 높은 ARC 명 수
	hi_win += cnt * lower
	draw += cnt * equal
	arc_win += cnt * higher

print(hi_win, arc_win, draw)
