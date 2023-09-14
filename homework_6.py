import datetime
import time
from os import system, name
item_1 = "⬛"
space = "  "
zero = [[item_1, item_1, item_1, item_1, item_1],
        [item_1, space, space, space, item_1],
        [item_1, space, space, space, item_1],
        [item_1, space, space, space, item_1],
        [item_1, item_1, item_1, item_1, item_1]]

one = [[space, space, space, space, item_1],
       [space, space, item_1, space, item_1],
       [item_1, space, space, space, item_1],
       [space, space, space, space, item_1],
       [space, space, space, space, item_1]]

two = [[item_1, item_1, item_1, item_1, item_1],
       [space, space, space, space, item_1],
       [item_1, item_1, item_1, item_1, item_1],
       [item_1, space, space, space, space],
       [item_1, item_1, item_1, item_1, item_1]]

three = [[item_1, item_1, item_1, item_1, item_1],
         [space, space, space, space, item_1],
         [item_1, item_1, item_1, item_1, item_1],
         [space, space, space, space, item_1],
         [item_1, item_1, item_1, item_1, item_1]]

four = [[item_1, space, space, space, item_1],
        [item_1, space, space, space, item_1],
        [item_1, item_1, item_1, item_1, item_1],
        [space, space, space, space, item_1],
        [space, space, space, space, item_1]]

five = [[item_1, item_1, item_1, item_1, item_1],
        [item_1, space, space, space, space],
        [item_1, item_1, item_1, item_1, item_1],
        [space, space, space, space, item_1],
        [item_1, item_1, item_1, item_1, item_1]]

six = [[space, space, space, space, item_1],
       [space, space, item_1, space, space],
       [item_1, item_1, item_1, item_1, item_1],
       [item_1, space, space, space, item_1],
       [item_1, item_1, item_1, item_1, item_1]]

seven = [[item_1, item_1, item_1, item_1, item_1],
         [space, space, item_1, space, space],
         [item_1, space, space, space, space],
         [item_1, space, space, space, space],
         [item_1, space, space, space, space]]

eight = [[item_1, item_1, item_1, item_1, item_1],
         [item_1, space, space, space, item_1],
         [item_1, item_1, item_1, item_1, item_1],
         [item_1, space, space, space, item_1],
         [item_1, item_1, item_1, item_1, item_1]]

nine = [[item_1, item_1, item_1, item_1, item_1],
        [item_1, space, space, space, item_1],
        [item_1, item_1, item_1, item_1, item_1],
        [space, space, item_1, space, space],
        [item_1, space, space, space, space]]

delimiter_0 = [space, space, space]
delimiter_1 = [space, item_1, space]

space_1 = ["   "]

numbers_dictionary = [zero, one, two, three,
                      four, five, six, seven, eight, nine]

rows_number = len(zero)


def print_time(h1, h2, m1, m2, s1, s2, runner):
    i = 0
    while i < rows_number:
        if runner == i:
            delimiter = delimiter_1
        else:
            delimiter = delimiter_0
        line = numbers_dictionary[h1][i] + space_1 + numbers_dictionary[h2][i] + delimiter + numbers_dictionary[m1][i] + \
            space_1 + numbers_dictionary[m2][i] + delimiter + \
            numbers_dictionary[s1][i] + space_1 + numbers_dictionary[s2][i]
        print("".join(line))
        i = i + 1


def get_current_time():
    date_now = datetime.datetime.now()
    hours = int(date_now.strftime("%H"))
    minutes = int(date_now.strftime("%M"))
    seconds = int(date_now.strftime("%S"))

    h2 = hours % 10
    h1 = hours // 10

    m2 = minutes % 10
    m1 = minutes // 10

    s2 = seconds % 10
    s1 = seconds // 10
    return [h1, h2, m1, m2, s1, s2]


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


n = 1
while n != 0:
    clear()
    [h1, h2, m1, m2, s1, s2] = get_current_time()
    print_time(h1, h2, m1, m2, s1, s2, n % rows_number)
    time.sleep(1)
    n += 1
