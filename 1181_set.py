import sys

N = int(sys.stdin.readline().rstrip())

words = ['' for _ in range(N)]

for i in range(N):
    words[i] = str(sys.stdin.readline().rstrip())
    
sorted_words = sorted(set(words), key=lambda x : (len(x), x))

for i in range(len(sorted_words)):
    print(sorted_words[i])