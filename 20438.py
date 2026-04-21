import sys

input = sys.stdin.readline

N, K, Q, M = map(int, input().split())

SLEEPING = [False] * (N + 3)
for x in map(int, input().split()):
    SLEEPING[x] = True

SEND_TO = list(map(int, input().split()))

CHECKED = [False] * (N + 3)

for start in SEND_TO:
    if SLEEPING[start]:
        continue
    
    for target in range(start, N + 3, start):
        if not SLEEPING[target]:
            CHECKED[target] = True

# PREFIX_SUM[i] = 3번부터 i번까지 '출석하지 않은' 학생의 총합
PREFIX_SUM = [0] * (N + 3)
for i in range(3, N + 3):
    # 현재 학생이 출석하지 않았다면 1, 했다면 0을 더함
    not_attended = 1 if not CHECKED[i] else 0
    PREFIX_SUM[i] = PREFIX_SUM[i-1] + not_attended

results = []
for _ in range(M):
    S, E = map(int, input().split())
    results.append(str(PREFIX_SUM[E] - PREFIX_SUM[S-1]))

print("\n".join(results) + "\n")
