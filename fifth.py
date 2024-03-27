with open('history_mirror.csv', 'r', encoding='utf-8') as file:
    data = []
    file.readline()
    for line in file:
        date, name, verdict = line.strip().split(',')
        temp = {'date': date, 'name': name, 'verdict': verdict}
        data.append(temp)


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet += alphabet.upper()
alphabet += ' '


def hash_user(username):
    '''
    Функция, вычисляющая хэш значение для данного имени пользователя
    :param username: фио пользователя
    :return: хэш значение фио
    '''
    p = 67
    m = 10 ** 9 + 9
    hash_value = 0
    for i in range(len(username)):
        idx = alphabet.index(username[i]) + 1
        val = (idx * p ** i) % m
        hash_value += val
    return hash_value


with open('users_with_hash.csv', 'w', encoding='utf-8') as file:
    print('ID,date,username,verdict', file=file)
    for el in data:
        ID = str(hash_user(el['name']))
        print(','.join([ID, el['date'], el['name'], el['verdict']]), file=file)
