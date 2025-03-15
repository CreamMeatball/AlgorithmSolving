name = input().strip()

# 빈도수를 계산
freq = {}
for ch in name:
    freq[ch] = freq.get(ch, 0) + 1

# 홀수 개 문자가 2개 이상이면 팰린드롬 불가능
odd_count = sum(v % 2 for v in freq.values())
if odd_count > 1:
    print("I'm Sorry Hansoo")
    exit()

# 팰린드롬 만들기
middle_char = ''
left_half = []
for ch in sorted(freq.keys()):
    if freq[ch] % 2 == 1:
        middle_char = ch
    left_half.append(ch * (freq[ch] // 2))

left_str = ''.join(left_half)
palindrome = left_str + middle_char + left_str[::-1]
print(palindrome)