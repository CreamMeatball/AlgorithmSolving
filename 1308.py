from datetime import date

def is_gg(y1, m1, d1, y2, m2, d2):
    if (y2 - y1) > 1000:
        return True
    if (y2 - y1) == 1000:
        if (m2 > m1) or (m2 == m1 and d2 >= d1):
            return True
    return False

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# 천년 이상 지속되는지 여부 검사
if is_gg(y1, m1, d1, y2, m2, d2):
    print("gg")
else:
    day1 = date(y1, m1, d1) # ex) print(day1) -> 2021-01-01
    day2 = date(y2, m2, d2)
    difference = (day2 - day1).days # ex) print(day2 - day1) -> 26 days, 0:00:00
    print(f"D-{difference}")