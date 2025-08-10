import sys

input = sys.stdin.readline

T = int(input().rstrip())

def find(parents, x):
    if parents[x] != x:
        # return find(parents, parents[x])
        parents[x] = find(parents, parents[x]) # 경로 압축. 매우 중요! (시간 절약)
    return parents[x]

def union(parents, a, b):
    parent_a = find(parents, a)
    parent_b = find(parents, b)
    if parent_a < parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b

for _ in range(T):
    N = int(input().rstrip())
    enemies = []
    for i in range(N):
        x, y, R = map(int, input().rstrip().split())
        enemies.append((i, x, y, R))
        
    # x 기준 정렬 (후보쌍 줄이기 위한 스윕)
    enemies.sort(key=lambda x: x[1])
    Rmax = max((r for _, _, _, r in enemies), default = 0)
        
    parents = [i for i in range(N)]
        
    for i in range(N - 1):
        n1, x1, y1, R1 = enemies[i]
        Rlimit = R1 + Rmax
        for j in range(i + 1, N):
            n2, x2, y2, R2 = enemies[j]
            if abs(x1 - x2) > Rlimit: # x거리만으로 봤을 때 최대한의 R로도 절대 닿을 수 없는 경우
                break # 현재의 i단계에서의 이후 j 모두 취소. 앞에서 x 오름차순으로 정렬했기 때문에 가능. 시간 초과 방지.
            # distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            distance = (x1 - x2)**2 + (y1 - y2)**2 # 속도 위해서 sqrt 안 쓰기
            if distance <= (R1 + R2)**2:
                union(parents, n1, n2)
            
    groups = {find(parents, i) for i in range(N)}
    print(len(groups))