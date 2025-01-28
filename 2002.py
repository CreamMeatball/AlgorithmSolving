import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())

car_list = []

in_car = {}
for i in range(N):
    car_name = str(input_data().rstrip())
    car_list.append(car_name)
    if car_name not in in_car:
        in_car[car_name] = []
    for car_key in in_car:
        if car_key == car_name:
            continue
        in_car[car_key].append(car_name)
    
out_car = {}
for i in range(N):
    car_name = str(input_data().rstrip())
    if car_name not in out_car:
        out_car[car_name] = []
    for car_key in out_car:
        if car_key == car_name:
            continue
        out_car[car_key].append(car_name)
        
# print(in_car)
# print(out_car)
    
count = 0
pass_car_list = []

for in_car_key in in_car:
    for car in in_car[in_car_key]:
        if car not in out_car[in_car_key] and car not in pass_car_list:
            count += 1
            pass_car_list.append(car)

print(count)
    
