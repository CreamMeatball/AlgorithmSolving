import sys

N = int(sys.stdin.readline().rstrip())

users = [-1 for _ in range(N)]

for i in range(N):
    users[i] = list(sys.stdin.readline().rstrip().split())
    
# 나이가 같을 경우 시간 순서로 정렬하는 건 굳이 안해도 됨. 그대로 놔두면 애초에 시간 순으로 정렬돼있기 때문에.
users.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(users[i][0], users[i][1])