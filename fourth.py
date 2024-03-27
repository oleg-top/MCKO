with open('history_mirror.csv', 'r', encoding='utf-8') as file:
    data = []
    file.readline()
    for line in file:
        date, name, verdict = line.strip().split(',')
        temp = {'date': date, 'name': name, 'verdict': verdict}
        data.append(temp)


used = {}
for el in data:
    year = el['date'].split('-')[0]
    if year in used.keys():
        used[year].append(el)
    else:
        used[year] = [el]

for key in sorted(used.keys()):
    print(f'В {key} году зеркало было использовано {len(used[key])}.')
