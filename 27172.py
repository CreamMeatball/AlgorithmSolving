N = int(input())
numbers = list(map(int, input().split()))
max_num = 0
player_scores = {}
for i, num in enumerate(numbers):
    if num > max_num:
        max_num = num
    player_scores[num] = 0
    
numbers.sort()

for num in numbers:
    for multiplied_num in range(num * 2, max_num + 1, num):
        if player_scores[multiplied_num]:
            player_scores[multiplied_num] -= 1
            player_scores[num] += 1
            
for key, value in player_scores.items():
    print(value, end=' ')