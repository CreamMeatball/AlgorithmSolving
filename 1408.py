from datetime import datetime

current = str(input())
current = datetime.strptime(current, "%H:%M:%S")

start = str(input())
start = datetime.strptime(start, "%H:%M:%S")

result = start - current
    
result = int(result.total_seconds())
hours = result // 3600
if hours < 0:
    hours = 24 + hours
minutes = (result % 3600) // 60
seconds = result % 60
formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
print(formatted_time)