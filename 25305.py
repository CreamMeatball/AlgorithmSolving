N, k = map(int, input().split())
x = list(map(int, input().split()))
sorted_x = sorted(x)

print(sorted_x[-k])