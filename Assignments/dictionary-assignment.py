handle = open('romeo.txt')
hours = dict()
hours_sorted = list()
for line in handle:
    times = line.rstrip()
    hour = times[-13:-11]
    hours_sorted.append(hour)
hours_sorted.sort()
for item in hours_sorted:
    hours[item] = hours.get(item, 0) + 1

for k, v in hours.items():
    print(k, v)
