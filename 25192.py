import sys
# from collections import deque

N = int(sys.stdin.readline().rstrip())

# hellolist = deque()
hellolist = set()
count = 0

for _ in range(N):
    chat = sys.stdin.readline().rstrip()
    if chat == "ENTER":
        hellolist.clear()
    else:
        if chat not in hellolist:
            hellolist.add(chat)
            count += 1
        else:
            continue
        
print(count)