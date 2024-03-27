with open('history_mirror.csv', 'r', encoding='utf-8') as file:
    data = []
    file.readline()
    for line in file:
        date, name, verdict = line.strip().split(',')
        temp = {'date': date, 'name': name, 'verdict': verdict}
        if temp['verdict'] == 'Победа над смертью':
            data.append(temp)

with open('mirror_error.csv', 'w', encoding='utf-8') as file:
    counter = 0
    for el in data:
        fn = el['name'].split()
        res = fn[0] + ' ' + fn[1][0] + '.' + fn[2][0] + '.'
        if counter == 0:
            print(f'Сообщение было зафиксировано: {el["date"]} у пользователя {res}')
        print(f'Сообщение было зафиксировано: {el["date"]} у пользователя {res}', file=file)
        counter += 1

