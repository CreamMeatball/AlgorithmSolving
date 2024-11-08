import sys
# from collections import deque

N, M = map(int, sys.stdin.readline().split())

words = dict()

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
    
# lambda 를 통한 다중 조건 정렬
words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])