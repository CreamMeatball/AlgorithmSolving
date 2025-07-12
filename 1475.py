import math
import sys

s = sys.stdin.readline().strip()

counts = [0] * 10
for ch in s:
    counts[int(ch)] += 1

six_nine_total = counts[6] + counts[9]
six_nine_needed = math.ceil(six_nine_total / 2)

counts[6] = counts[9] = six_nine_needed

print(max(counts))
