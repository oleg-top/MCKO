with open('history_mirror.csv', 'r', encoding='utf-8') as file:
    data = []
    file.readline()
    for line in file:
        date, name, verdict = line.strip().split(',')
        temp = {'date': date, 'name': name, 'verdict': verdict}
        if temp['verdict'] == 'Победа над смертью':
            data.append(temp)

with open('mirror_error.csv', 'w', encoding='utf-8') as file:
    print('date,username', file=file)
    for el in data:
        print(f'{el["date"]},{el["name"]}', file=file)

el = min(data, key=lambda x: (int(x['date'].split('-')[0]), int(x['date'].split('-')[1]), int(x['date'].split('-')[2])))
fn = el['name'].split()
res = fn[0] + ' ' + fn[1][0] + '.' + fn[2][0] + '.'
print(f'Сообщение было зафиксировано: {el["date"]} у пользователя {res}')
