ab = input()
min_b = float('inf')
window = ab.count('a') # 윈도우 크기를 a의 개수로 설정
# 왜냐면 결국 a가 다 뭉쳐야되니까, 뭉쳤을 때 총 길이를 슬라이딩 윈도우에서 윈도우 길이로 쓰자.
# 그래서 윈도우 안에 존재하는 b 개수를 다 세서, 해당 b들을 바깥으로 모두 빼버리면 a만 남게 되는 거니까.

len_ = len(ab)
for i in range(len_):
    current_b = 0
    for j in range(window): # 윈도우 안에 있는 빼내야 할 b의 개수 확인
        index = (i + j) % len_
        if ab[index] == "b":
            current_b += 1
    if current_b < min_b:
        min_b = current_b

print(min_b)