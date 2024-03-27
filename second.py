def bubble_sort(arr):
    """
    Сортирует данный список при помощи алогоритма Bubble sort
    :param arr: исходный список
    :return: отсортированный список
    """
    for k in range(0, len(arr)):
        for i in range(0, len(arr) - 1):
            for j in range(i, len(arr) - i - 1):
                if arr[j]['verdict'] > arr[j + 1]['verdict']:
                    arr[j]['verdict'], arr[j + 1]['verdict'] = arr[j + 1]['verdict'], arr[j]['verdict']
    return arr


with open('history_mirror.csv', 'r', encoding='utf-8') as file:
    data = []
    file.readline()
    for line in file:
        date, name, verdict = line.strip().split(',')
        temp = {'date': date, 'name': name, 'verdict': verdict}
        data.append(temp)

ds = bubble_sort(data)[:4]
for el in ds:
    print(f'{el["date"]} - {el["name"]} - {el["verdict"]}')
