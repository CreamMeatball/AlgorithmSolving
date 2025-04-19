# solving with Tree structure using AI

expression = input().strip()

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(infix):
    # 연산자 우선순위 정의
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    
    # 스택 초기화
    operator_stack = [] # 연산자 스택
    operand_stack = [] # 피연산자(알파벳) 스택
    
    i = 0
    while i < len(infix):
        if infix[i].isalpha(): # isalpha(): 알파벳인지 확인
            # 피연산자(알파벳)는 노드로 만들어 피연산자 스택에 저장
            operand_stack.append(Node(infix[i]))
        elif infix[i] == '(':
            operator_stack.append(infix[i])
        elif infix[i] == ')':
            # 여는 괄호가 나올 때까지 연산 수행
            while operator_stack and operator_stack[-1] != '(':
                create_subtree(operator_stack, operand_stack)
                # stack의 가장 끝에 있는 연산자와 피연산자로 서브트리 만들고, 생성된 서브트리를 피연산자 스택에 추가
            operator_stack.pop()  # '(' 제거
        else:  # 연산자인 경우
            # 현재 연산자보다 우선순위가 높은 연산자들 처리
            while (operator_stack and operator_stack[-1] != '(' and # 여는 괄호가 나올 때까지 수행
                   precedence[operator_stack[-1]] >= precedence[infix[i]]):
                # 앞에 존재하는 연산자와 피연산자 덩어리들을 합쳐 서브 트리 하나로 응집
                create_subtree(operator_stack, operand_stack)
            operator_stack.append(infix[i])
        i += 1
    
    # 남은 연산자 처리
    while operator_stack:
        create_subtree(operator_stack, operand_stack)
    
    # 최종 트리의 루트 반환
    return operand_stack[0] if operand_stack else None

def create_subtree(operator_stack, operand_stack):
    # 연산자를 루트로 하는 서브트리 생성
    operator = operator_stack.pop()
    root = Node(operator)
    
    # 오른쪽 자식과 왼쪽 자식을 연결 (순서 주의: 스택이므로 오른쪽을 먼저 pop)
    right = operand_stack.pop()
    left = operand_stack.pop()
    
    root.right = right
    root.left = left
    
    # 새 서브트리를 피연산자 스택에 추가
    operand_stack.append(root) # class type인 Node가 추가되는 것.

def postorder_traversal(node, result):
    # 재귀 방식이되 호출 순서를 Left(재귀 호출) Right(재귀 호출) Root(재귀 끝난 뒤 append) 대로.
    if node:
        postorder_traversal(node.left, result)  # 왼쪽 서브트리 순회
        postorder_traversal(node.right, result)  # 오른쪽 서브트리 순회
        result.append(node.value)  # 현재 노드의 값 추가
    return result

# 식 트리 구축
tree_root = build_expression_tree(expression)

# 후위 순회를 통해 후위 표기식 생성
postfix_result = postorder_traversal(tree_root, [])
print(''.join(postfix_result))