import sys

while(True):
    input_text = sys.stdin.readline().rstrip()
    if input_text == ".":
        break
    stack = []
    answer = "yes"
    
    input_text = list(input_text)
    for i in input_text:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                answer = "no"
                break
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                answer = "no"
                break
    if stack:
        answer = "no"
    print(answer)