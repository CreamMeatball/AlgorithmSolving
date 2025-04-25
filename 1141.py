import sys
from itertools import combinations

input_data = sys.stdin.readline

N = int(input_data().rstrip())

words = []

for _ in range(N):
    words.append(input_data().rstrip())

words = list(set(words))
# words.sort(key=lambda x: len(x))
# words.sort(key=len)

result = []

for word in words:
    # 현재 단어가 다른 단어의 접두사가 되는지
    is_prefix = False
    for word2 in words:
        if word == word2:
            continue
        if word2.startswith(word):
            # print(f"{word} is prefix for {word2}")
            is_prefix = True
    
    if not is_prefix:
        result.append(word)
        
print(len(result))