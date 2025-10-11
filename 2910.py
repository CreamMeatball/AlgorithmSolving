N, C = map(int, input().split())
nums = list(map(int, input().split()))

freq = {}
first_idx = {}
for i, x in enumerate(nums):
    freq[x] = freq.get(x, 0) + 1
    if x not in first_idx:
        first_idx[x] = i

sorted_keys = sorted(freq.keys(), key=lambda x: (-freq[x], first_idx[x]))

out = []
for k in sorted_keys:
    out.extend([str(k)] * freq[k])

print(" ".join(out))