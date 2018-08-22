input_string = input()
travel = input_string.split(" ")
travel.sort(key=int)
travel_skip = 0
travel_time = 0
travel_start = int(travel[0])
travel_end = int(travel[1])

if travel_start % 2 == 1 and travel_end % 2 == 0:
    travel_skip += 1
elif travel_start % 2 == 0 and travel_end % 2 == 1:
    travel_skip += 1

travel_time = int((travel_end - travel_start) / 2 + travel_skip)
print(travel_time)
