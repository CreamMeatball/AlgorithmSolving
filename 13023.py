import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

friendTo = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    friendTo[a].append(b)
    friendTo[b].append(a) # '3 7' 주어졌으면 '7 -> 3' 으로도 친구 관계임.
    
# for key, value in friendTo.items():
#     print(f"{key}: {value}")
    
def dfs(selected: set, select):
    if len(selected) == 5:
        # print(f"answer relationship: {selected}")
        print(1)
        sys.exit()
    for f in friendTo[select]:
        if f not in selected:
            selected.add(f)
            dfs(selected, f)
    selected.remove(select)
    

for i in range(N):
    dfs(set([i]), i)
    
print(0)