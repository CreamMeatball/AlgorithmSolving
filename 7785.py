n = int(input())
personnel = set()
for i in range(n):
    input_data = str(input())
    person, enter_or_leave = input_data.split()
    if enter_or_leave == 'enter':
        personnel.add(person)
    elif enter_or_leave == 'leave':
        personnel.remove(person)
        
print("\n".join(f"{data}" for data in sorted(personnel, reverse=True)))