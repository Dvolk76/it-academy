# 1. Сколько было всего запросов
# 2. Сколько уникальных ip адресов обратилось ( 4 числа, разделенные точкой, в начале строки)
# 3. Какие браузеры обращались. Для простоты берем запись почти в конце строки (Firefox/34.0) и подобное
# 4. Сколько запросов от каждого такого браузера


fp = open("log5000.txt", 'r')
i = 0
ip = []
brows = []
while True:
    i = i + 1
    for line in fp.readlines():
        print(line.split())
        xxx = line.split()
        ip.append(xxx[0])
        brows.append(xxx[-2])
        brows_s = set(brows)
        print("всего запросов", len(ip))
        yyy = set(ip)
        print("всего уникальных ип", len(yyy))
        print(len(brows_s))

