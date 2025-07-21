import sys

input = sys.stdin.readline

N = int(input().rstrip())
works = {}
for i in range(1, N + 1):
    works[i] = list(map(int, input().rstrip().split()))
    
cost = 0
