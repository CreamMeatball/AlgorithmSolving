import sys
sys.setrecursionlimit(10 ** 6)

preorder = []
while True:
    try:
        line = input()
        if not line:
            break
        preorder.append(int(line))
    except EOFError:
        break
    
# preorder로 받았을 때 그걸로 트리를 구성하려면
# 트리의 루트를 노드로 구성한 뒤
# 노드의 왼쪽이 존재하지 않을 경우, 왼쪽에 노드로 삽입하고
# 왼쪽이 존재할 경우, 왼쪽 노드에 다시 재귀적으로 삽입하는 방식으로 구현
# 오른쪽도 마찬가지

# preorder로 탐색한 걸로 트리를 구성하려면
# preorder로 탐색할 때랑 같은 순서로 삽입해서 트리 구성하면 됨

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value): # preorder 순회로 값을 받았기 때문에, 아래처럼 insert 메소드 구현
        if value < self.value: # BST니까 값이 작을 경우 왼쪽
            # root로부터 타고 내려가면서 현재 노드 위치에서 왼쪽 노드를 갖고 있지 않을 경우에 value를 Node로 삽입
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value) # 재귀적으로 왼쪽 노드에 삽입
        else: # BST니까 값이 클 경우 오른쪽
            # root로부터 타고 내려가면서 현재 노드 위치에서 오른쪽 노드를 갖고 있지 않을 경우에 value를 Node로 삽입
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value) # 재귀적으로 오른쪽 노드에 
                
def build_tree(preorder):
    if not preorder:
        return None
    root = Node(preorder[0])
    for value in preorder[1:]:
        root.insert(value) # 가장 위 root 노드쪽으로 값을 삽입.
    return root # root: preorder[0]을 루트로 하는 전체 트리

def postorder_traversal(node): # postorder 탐색 (재귀)
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value)
        
postorder_traversal(build_tree(preorder))