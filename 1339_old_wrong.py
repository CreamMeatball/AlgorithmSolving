N = int(input())

# GCF + ACDEB
# 783 + 98654
# = 99437

# GCF + ACDEB
# 683 + 98754
# = 99437

Words = [0]*N

for i in range(N):
    Words[i] = list(input())[::-1]
    # 한 글자씩 잘라서, 역순으로( ::-1 ) 넣기
    # 자릿수의 최대값을 따로 계산해서 판별하지 않기 위해 편하게 역순으로 정렬 후 자릿수 연산

# 우선순위 :
# 자릿수가 높은 문자
# 자릿수가 같을 경우, 더 많이 나오는 문자

# 집합 자료형을 이용하여 중복 없애서 넣기
word_list = set([])
for i in range(N):
    for j in range(len(Words[i])):
        word_list.add(Words[i][j])
        
# 인덱싱을 위해 집합 자료형을 리스트로 변환
word_list = list(word_list)
        
# print(word_list)

# 각 알파벳당 우선순위 정리를 위한 사전 자료형 변수
word_list_priority = dict()
for i in range(len(word_list)):
    word_list_priority[word_list[i]] = 0

# print(word_list_priority)

# 우선순위 넣기(1). 자릿수*1만
for i in range(N):
    for j in range(len(Words[i])):
        if Words[i][j] in word_list:
            if word_list_priority[Words[i][j]] < (j+1)*10000: word_list_priority[Words[i][j]] = (j+1)*10000
            
# print(word_list_priority)

# 우선순위 넣기(2). 알파벳이 한 번 나온 횟수마다 +1
for i in range(N):
    for j in range(len(Words[i])):
        word_list_priority[Words[i][j]] += 1
        
# print(word_list_priority)

# wlp = word_list_priority를 value값 기준으로 내림차순 정렬한 리스트(key 값만 남음)
wlp = dict(sorted(word_list_priority.items(), key=lambda x:x[1]))
wlp = sorted(wlp, reverse=True, key=lambda x:wlp[x])

# print(wlp)
# print(type(wlp))

# 내림차순 정렬된 wlp를 이용하여 word_list_priority의 각각의 알파벳에 실제로 대체하게 될 숫자로 변경. e.g. A = 9
for i in range(len(wlp)):
    word_list_priority[wlp[i]] = 9-i

# print(word_list_priority)

# 최종적으로 알파벳을 숫자로 대체
for i in range(N):
    for j in range(len(Words[i])):
        Words[i][j] = word_list_priority[Words[i][j]]
        
# print(Words)

result = 0

# 숫자로 대체된 리스트를 합해서 결과 내기
for i in range(N):
    for j in range(len(Words[i])):
        result += (10**j)*int(Words[i][j])
        
print(result)