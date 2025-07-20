import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)

N = int(input())
parents = list(map(int, input().split()))
remove = int(input())

children = defaultdict(list)
for i in range(N):
    children[parents[i]].append(i)
    
# print(children)

root = parents.index(-1)

if root == remove:
    print(0)
    sys.exit()

# [1번 풀이]
def dfs(node):
    if node == remove:
        return 0

    valid_children = [c for c in children[node] if c != remove]

    if not valid_children:
        return 1

    return sum(dfs(c) for c in valid_children)

print(dfs(root))

# [2번 풀이]
# children.pop(remove, None) # KeyError 방지용 pop

# p = parents[remove]
# if p in children:
#     children[p].remove(remove)

# def dfs(node):
#     if not children[node]:
#         return 1
#     return sum(dfs(c) for c in children[node])

# print(dfs(root))