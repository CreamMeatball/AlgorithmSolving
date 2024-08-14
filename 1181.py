import sys

N = int(sys.stdin.readline().rstrip())

words = ['' for _ in range(N)]

for i in range(N):
    words[i] = str(sys.stdin.readline().rstrip())
    
words.sort(key=lambda x : (len(x), x))

for i in range(N):
    if(i != N-1):
        if(words[i] != words[i+1]):
            print(words[i])
    else:
        print(words[i])