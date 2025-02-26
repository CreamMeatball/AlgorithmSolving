N, newScore, P = map(int, input().split())
if N > 0:
    highscores = list(map(int, input().split()))
else:
    highscores = []

testPrint = False

highscores.append(newScore)
highscores.sort(reverse=True)

print(f"scores: {highscores}") if testPrint else None

lenOfHighscore = dict()
for highscore in highscores:
    lenOfHighscore[highscore] = lenOfHighscore.get(highscore, 0) + 1
    
print(f"lenOfScores: {lenOfHighscore}") if testPrint else None

rank = dict()
rankCount = 1

for highscore in lenOfHighscore.keys():
    rank[highscore] = rankCount
    rankCount += lenOfHighscore[highscore]
    
print(f"rank: {rank}") if testPrint else None

sumTillNewScore = 0

for highscore, value in lenOfHighscore.items():
    sumTillNewScore += value
    if highscore == newScore:
        break
    
print(f"number of scores include new Score: {sumTillNewScore}") if testPrint else None
    
if sumTillNewScore <= P:
    print(rank[newScore])
else:
    print(-1)