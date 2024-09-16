string = str(input())

alphabet = [0 for _ in range(26)]

for s in string:
    s = s.lower()
    alphabet[ord(s) - 97] += 1
    
maximum = max(alphabet)
    
if alphabet.count(maximum) != 1:
    print("?")
else:
    print(chr(alphabet.index(maximum)+97).upper())