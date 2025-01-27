import sys

input_data = sys.stdin.readline
N = int(input_data().rstrip())

NodeData = {}
for _ in range(N):
    node, left, right = input_data().rstrip().split()
    NodeData[node] = [left, right]
    
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(NodeData[node][0])
    preorder(NodeData[node][1])
    
def inorder(node):
    if node == '.':
        return
    inorder(NodeData[node][0])
    print(node, end='')
    inorder(NodeData[node][1])
    
def postorder(node):
    if node == '.':
        return
    postorder(NodeData[node][0])
    postorder(NodeData[node][1])
    print(node, end='')
    
preorder('A')
print()
inorder('A')
print()
postorder('A')