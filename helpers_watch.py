from variables_watch import space_1, rows_number, numbers_dictionary, delimiters_dictionary, color
from os import system, name
import datetime
import time


def get_current_time():
    date_now = datetime.datetime.now()
    time_now = date_now.strftime("%H%M%S")
    h1 = int(time_now[0])
    h2 = int(time_now[1])
    m1 = int(time_now[2])
    m2 = int(time_now[3])
    s1 = int(time_now[4])
    s2 = int(time_now[5])
    return [h1, h2, m1, m2, s1, s2]


def print_time(h1, h2, m1, m2, s1, s2, n):
    i = 0
    k = n % len(delimiters_dictionary)
    while i < rows_number:
        line = numbers_dictionary[h1][i] + space_1 + numbers_dictionary[h2][i] + \
            delimiters_dictionary[k][i] + numbers_dictionary[m1][i] + \
            space_1 + numbers_dictionary[m2][i] + delimiters_dictionary[k][i] + \
            numbers_dictionary[s1][i] + space_1 + numbers_dictionary[s2][i]
        print(color[k] + "".join(line))

        i = i + 1


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
