import sys

N = int(sys.stdin.readline().rstrip())
rainbowDance = set()
rainbowDance.add("ChongChong")

for _ in range(N):
    people = list(sys.stdin.readline().split())
    if (people[0] in rainbowDance) or (people[1] in rainbowDance):
        rainbowDance.add(people[0])
        rainbowDance.add(people[1])
    else:
        continue
    
print(len(rainbowDance))