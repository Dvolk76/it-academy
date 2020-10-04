import datetime
import time
import os

l_0 = {
    0: '███████',
    1: '     ██',
    2: '███████',
    3: '███████',
    4: '█     █',
    5: '███████',
    6: '███████',
    7: '███████',
    8: '███████',
    9: '███████'
}

l_1 = {
    0: '█     █',
    1: '      █',
    2: '      █',
    3: '      █',
    4: '█     █',
    5: '█      ',
    6: '█      ',
    7: '      █',
    8: '█     █',
    9: '█     █'
}

l_2 = {
    0: '█     █',
    1: '      █',
    2: '███████',
    3: ' ██████',
    4: '███████',
    5: '███████',
    6: '███████',
    7: '      █',
    8: '███████',
    9: '███████'
}

l_3 = {
    0: '█     █',
    1: '      █',
    2: '█      ',
    3: '      █',
    4: '      █',
    5: '      █',
    6: '█     █',
    7: '      █',
    8: '█     █',
    9: '      █',
}
l_4 = {
    0: '███████',
    1: '      █',
    2: '███████',
    3: '███████',
    4: '      █',
    5: '███████',
    6: '███████',
    7: '      █',
    8: '███████',
    9: '███████'
}


def get_current_time():
    now = datetime.datetime.now()
    now_str = str(now)
    current_time = now_str[11:19]
    return current_time


def print_digits(time_now):
    hour_1 = int(time_now[0])
    hour_2 = int(time_now[1])
    min_1 = int(time_now[3])
    min_2 = int(time_now[4])
    sec_1 = int(time_now[6])
    sec_2 = int(time_now[7])
    if int(time_now[7]) % 2 == 0:
        a = ' █ '
    else:
        a = '   '

    print(l_0[hour_1], l_0[hour_2], '   ', l_0[min_1], l_0[min_2], '   ', l_0[sec_1], l_0[sec_2])
    print(l_1[hour_1], l_1[hour_2], a, l_1[min_1], l_1[min_2], a, l_1[sec_1], l_1[sec_2])
    print(l_2[hour_1], l_2[hour_2], '   ', l_2[min_1], l_2[min_2], '   ', l_2[sec_1], l_2[sec_2])
    print(l_3[hour_1], l_3[hour_2], a, l_3[min_1], l_3[min_2], a, l_3[sec_1], l_3[sec_2])
    print(l_4[hour_1], l_4[hour_2], '   ', l_4[min_1], l_4[min_2], '   ', l_4[sec_1], l_4[sec_2],)
    print('\n')

def clear_screen():
    os.system("clear")


def sleep_for_a_while(period):
    time.sleep(period)


if __name__ == '__main__':
    while True:
        time_now = str(get_current_time())
        print_digits(time_now)
        sleep_for_a_while(1)
        clear_screen()