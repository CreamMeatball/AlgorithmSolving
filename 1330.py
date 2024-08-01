# 파이썬 삼항연산자는 형식이 다름. 참값 if 조건 + else 거짓값
A, B = map(int, input().split())
print(">") if A > B else print("<") if A < B else print("==")