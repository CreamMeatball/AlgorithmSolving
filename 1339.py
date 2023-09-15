N = int(input())

Words = []
for _ in range(N):
    Words.append(list(input()))
    
# print(len(Words[1]))
    
word_list = dict()

for word in Words:
    # print("word : ", word)
    for spell_seq in range(len(word)):
        if word[spell_seq] not in word_list:
            word_list[word[spell_seq]] = 10 ** (len(word)-1 - spell_seq)
        else:
            word_list[word[spell_seq]] += 10 ** (len(word)-1 - spell_seq)

wl = sorted(word_list.items(), key=lambda x: x[1], reverse=True)

# wl 은 리스트 안에 튜플이 있는 구조가 된다.
# wl = [('A', 10000), ('C', 1010), ... , ('B', 1)]

for i in range(len(wl)):
    word_list[wl[i][0]] = 9 - i
    
# print(word_list)

result = 0

for word in Words:
    for i in range(len(word)):
        result += word_list[word[i]] * (10 ** (len(word)-1-i))
        
print(result)