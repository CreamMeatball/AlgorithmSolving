import sys

input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
a.sort()

pair_pref = [10**30] * (n + 1)
pair_pref[0] = 0
for i in range(2, n + 1, 2):
	pair_pref[i] = pair_pref[i - 2] + (a[i - 1] - a[i - 2])

pair_suf = [10**30] * (n + 1)
pair_suf[n] = 0
for i in range(n - 2, -1, -2):
	pair_suf[i] = pair_suf[i + 2] + (a[i + 1] - a[i])

answer = 10**30
for s in range(0, n - 2, 2):
	cost = pair_pref[s] + (a[s + 2] - a[s]) + pair_suf[s + 3]
	if cost < answer:
		answer = cost

print(answer)