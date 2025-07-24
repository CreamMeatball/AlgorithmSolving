N = int(input())
M = int(input())

# M이 엄청 커서 브루트포스로 구하면 시간 초과 날 듯

freqs = {
    1: [1],
    2: [2, 8],
    3: [3, 7],
    4: [4, 6],
    5: [5]
}

# 1234
# 5432
# 1234
# 5432
# ... 반복

freq = freqs[N]

cycle = M // len(freq) # 몇 번째 8길이 주기인지
within = M % len(freq) # 그 주기에서 몇 번째 등장인지

stop_pos = 8 * cycle + freq[within]
print(stop_pos - 1) # 그 직전까지 센 개수 출력