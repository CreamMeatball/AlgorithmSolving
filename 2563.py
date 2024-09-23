number = int(input())

paper = [[] for _ in range(number)]

for i in range(number):
    paper[i] = list(map(int, input().split()))
    
area = [[0 for _ in range(101)] for _ in range(101)]

for i in range(number):
    initial_x = paper[i][0]
    initial_y = paper[i][1]
    end_x = paper[i][0] + 10
    end_y = paper[i][1] + 10
    
    for x in range(initial_x, end_x):
        for y in range(initial_y, end_y):
            area[x][y] = 1
    # print(f"{initial_x} {initial_y} {end_x} {end_y} to 1")

# print(area.count(1)) # .count는 1차원에서만 된다고 함.

count = sum(row.count(1) for row in area)
print(count)