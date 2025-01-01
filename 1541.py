sentence = str(input())

sentence_sequence = []
point = 0

for i in range(len(sentence)):
    # print("i : ", i, "sentence[i] : ", sentence[i])
    if sentence[i] in ['+', '-']:
        sentence_sequence.append(int(sentence[point:i]))
        point = i + 1
        sentence_sequence.append(sentence[i])
        # print("numbers : ", numbers)
    elif i == len(sentence) - 1:
        sentence_sequence.append(int(sentence[point:]))
    else:
        continue
        
# print(sentence_sequence)

trigger = False

for i in range(len(sentence_sequence)):
    if sentence_sequence[i] == '-':
        trigger = True
        continue
    if trigger and sentence_sequence[i] == '+':
        sentence_sequence[i] = '-'
        
# print(sentence_sequence)

result = sentence_sequence[0]
for i in range(1, len(sentence_sequence)):
    if sentence_sequence[i] == '-':
        result -= sentence_sequence[i+1]
    elif sentence_sequence[i] == '+':
        result += sentence_sequence[i+1]
        
print(result)