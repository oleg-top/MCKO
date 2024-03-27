with open('history_mirror.csv', 'r', encoding='utf-8') as file:
    data = []
    file.readline()
    for line in file:
        date, name, verdict = line.strip().split(',')
        temp = {'date': date, 'name': name, 'verdict': verdict}
        data.append(temp)


def predict(name):
    '''
    Возвращает предсказания по данным имени и отчеству
    :param name: имя и отчество, записанные с большой буквы и через пробел
    :return: найденные предсказания
    '''
    res = []
    for el in data:
        nm = el['name'].split()
        if nm[1] == name.split()[0] and nm[2] == name.split()[1]:
            fn = el['name'].split()
            fullname = fn[0] + ' ' + fn[1][0] + '.' + fn[2][0] + '.'
            res.append(f'{fullname} - {el["verdict"]}')
    if len(res) == 0:
        res.append('Вас не нашлось в записях')
    return res


nameInput = input('Введите Ваши имя и отчество через пробел с большой буквы или "stop" для окончания работы: ')
while nameInput != 'stop':
    prediction = predict(nameInput)
    print(*prediction, sep='\n')
    nameInput = input('Введите Ваши имя и отчество через пробел с большой буквы или "stop" для окончания работы: ')