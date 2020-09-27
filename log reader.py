# 1. Сколько было всего запросов
# 2. Сколько уникальных ip адресов обратилось ( 4 числа, разделенные точкой, в начале строки)
# 3. Какие браузеры обращались. Для простоты берем запись почти в конце строки (Firefox/34.0) и подобное
# 4. Сколько запросов от каждого такого браузера

from collections import Counter
from pprint import pprint
fp = open("log5000.txt", 'r')
ip = []
browsers = []
browsers_names = {"Chrome": 0, "Safari": 0, "Firefox": 0, "Edge": 0, "Opera": 0}
while True:

    for line in fp.readlines():
        print(line.split())
        xxx = line.split()
        ip.append(xxx[0])
        browsers.append(xxx[-2])
        browsers_s = set(browsers)
        print("Всего запросов - ", len(ip))
        yyy = set(ip)
        print("Всего уникальных ip - ", len(yyy))
        print("Всего уникальных браузеров - ", len(browsers_s))
        d = dict.fromkeys(browsers_s)
        imena = d.keys()
        print('Обращались вот эти браузеры - ', imena)
        c = Counter(browsers)
        print('Вот сколько каждый браузер обратился раз - ')
        pprint(c)


