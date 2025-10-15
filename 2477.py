import sys

input = sys.stdin.readline

K = int(input().rstrip())

numbers = []

for _ in range(6):
    direction, length = map(int, input().rstrip().split())
    numbers.append([direction, length])
    
clockwise_cases = [(1, 3), (4, 1), (2, 4), (3, 2)]
    
for i in range(1, 7):
    d_prev = numbers[(i - 1) % 6][0]
    d_current = numbers[i % 6][0]
    if (d_prev, d_current) in clockwise_cases:
        width = numbers[(i - 3) % 6][1]
        height = numbers[(i - 4) % 6][1]
        concave_width = numbers[(i - 1) % 6][1]
        concave_height = numbers[i % 6][1]
        # print((width, height))
        # print((concave_width, concave_height))
        area = width * height - concave_width * concave_height
        print(area * K)
        break