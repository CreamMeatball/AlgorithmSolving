import sys

input = sys.stdin.readline

N, M, Q = map(int, input().split())

# 벽 내구도를 위치 배열로 저장한다.
# 그 배열의 누적합을 만든다.
# 그러면 임의 구간의 벽 내구도 합(= 그 구간을 뚫는 데 필요한 총 망치질)을 O(1)에 구할 수 있다.
# 이전 학생들이 부순 결과는 경계 2개로 관리한다.
# 왼쪽에서 어디까지 완전히 뚫렸는지
# 오른쪽에서 어디부터 완전히 뚫렸는지
# 매 학생 P에서
# 왼쪽 탈출 비용 = 아직 안 뚫린 구간 중 P 왼쪽 경로의 내구도 합
# 오른쪽 탈출 비용 = 아직 안 뚫린 구간 중 P 오른쪽 경로의 내구도 합
# 을 비교해서 규칙대로 방향 선택한다.
# 선택한 방향에 따라 경계를 갱신한다.
# 왼쪽 탈출이면 왼쪽 뚫린 구간을 P-1까지 확장
# 오른쪽 탈출이면 오른쪽 뚫린 구간을 P+1까지 확장
# 이렇게 하면 학생 1명당 O(1), 전체 O(N + M + Q)로 처리 가능.

dur = [0] * (N + 1)
for _ in range(M):
	w, d = map(int, input().split())
	dur[w] = d

prefix = [0] * (N + 1)
for i in range(1, N + 1):
	prefix[i] = prefix[i - 1] + dur[i]


def range_sum(l, r):
	if l > r:
		return 0
	return prefix[r] - prefix[l - 1]


left_cleared = 0
right_cleared_start = N + 1

result = []

for _ in range(Q):
	p = int(input())

	left_l = max(1, left_cleared + 1)
	left_r = min(p - 1, right_cleared_start - 1)
	left_hits = range_sum(left_l, left_r)

	right_l = max(p + 1, left_cleared + 1)
	right_r = min(N, right_cleared_start - 1)
	right_hits = range_sum(right_l, right_r)

	dist_left = p - 1
	dist_right = N - p

	choose_left = False
	if left_hits < right_hits:
		choose_left = True
	elif left_hits == right_hits:
		if dist_left < dist_right:
			choose_left = True
		elif dist_left == dist_right:
			choose_left = True

	if choose_left:
		result.append(str(left_hits))
		if p - 1 > left_cleared:
			left_cleared = p - 1
            # 벽을 다 뚫고 탈출하기 때문에, left_cleared 부터는 싹 다 모든 벽이 뚫려있음이 보증됨. --> 이 덕분에 left_cleared 라는 단일 스칼라 값만으로 누적합을 통한 잔존 cost 쉽게 계산할 수 있음
	else:
		result.append(str(right_hits))
		if p + 1 < right_cleared_start:
			right_cleared_start = p + 1

print("\n".join(result))
