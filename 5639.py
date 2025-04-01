import sys
sys.setrecursionlimit(10 ** 6)

# 입력 받기 (EOF까지)
preorder = []
while True:
    try:
        line = input()
        if line:
            preorder.append(int(line))
        else:
            break
    except EOFError:
        break

# 노드 클래스
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 검색 트리에 노드 삽입
def insert(root, value):
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value)

# 후위 순회
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)

# 트리 구성
root = Node(preorder[0])
for value in preorder[1:]:
    insert(root, value)

# 후위 순회 결과 출력
postorder(root)
