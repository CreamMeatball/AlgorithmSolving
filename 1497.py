import sys
from itertools import combinations

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())

guitars = {}
guitar_names = []
for _ in range(N):
    data = list(map(str, input_().rstrip().split()))
    guitar = data[0]
    playable = list(data[1])
    for i in range(M):
        if playable[i] == 'Y':
            playable[i] = int(1)
        else:
            playable[i] = int(0)
    guitars[guitar] = playable
    guitar_names.append(guitar)
    
def checkPlayable(gs: tuple):
    checklist = [0] * (M)
    for g in gs:
        for i in range(M):
            checklist[i] = int(checklist[i] or guitars[g][i])
    return sum(checklist) # 이 기타 조합으로 연주할 수 있는 곡 개수

guitar_combs = []

# guitar_combs.extend(tuple(guitar_names))
# for i in range(2, M + 1):
for i in range(1, N + 1):
    guitar_combs.extend(list(combinations(guitar_names, i)))
    
# print(guitar_combs)
    
max_songs = 0
count = 51

for gc in guitar_combs:
    playable_songs = checkPlayable(gc)
    if playable_songs:
        if playable_songs > max_songs:
            max_songs = playable_songs
            count = len(gc)
        elif playable_songs == max_songs:
            count = min(count, len(gc))
        
if count == 51:
    print(-1)
else:
    print(count)