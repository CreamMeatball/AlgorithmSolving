import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

truth = input().rstrip()
truth_people = []
if truth != 0:
    truth = list(map(int, truth.split()))
    truth, truth_people = truth[0], truth[1:]
    
parties = []
parent = [i for i in range(N + 1)] # 사람 i (index) 가 속한 파티 index

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root <= y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root
        
for _ in range(M):
    party = list(map(int, input().rstrip().split()))
    people = party[1:]
    parties.append(people)
    for i in range(party[0] - 1):
        union(people[i], people[i + 1])
        
# print(parent)

truth_parent = [0] + [find(i) for i in truth_people]

# print(truth_parent)

count = 0
for party in parties:
    if any(find(p) in truth_parent[1:] for p in party):
       continue
    count += 1
    
print(count)