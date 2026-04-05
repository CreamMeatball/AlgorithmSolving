import sys

input = sys.stdin.readline

N, K = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# min max(A 최종합,B 최종합)

def f(x, arr):
	l = s = m = 0
	for r, v in enumerate(arr):
		s += v
		while s > x:
			s -= arr[l]
			l += 1
		m = max(m, r - l + 1)
	return N - m

lo, hi = 0, max(sum(a), sum(b))

while lo < hi:
	mid = (lo + hi) // 2
	if f(mid, a) + f(mid, b) <= K:
		hi = mid
	else:
		lo = mid + 1
  
print(lo)