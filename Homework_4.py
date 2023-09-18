from random import randint, randrange
from os import system, name
from time import sleep
questions = [
    "Как называется разновидность воды, в которой атом водорода замещён его изотопом дейтерия?",
    "Что такое десница?",
    "В какое море впадает река Урал?",
    "На что кладут руку члены английского общества лысых во время присяги?",
    "Как назывался каменный монолит, на котором установлен памятник Петру I в Санкт-Петербурге?",
    "Как Пётр Ильич Чайковский назвал свою серенаду для скрипки с оркестром си-бемоль минор?",
    "Какого ордена не было у первого советского космонавта Юрия Гагарина?",
    "Какое животное имеет второе название — кугуар?",
    "Что в России 19 века делали в дортуаре?",
    "Какой химический элемент назван в честь злого подземного гнома?",
    {100: [(True, "Тяжёлая"), (False, "Лёгкая"),
           (False, "Средняя"), (False, "Невесомая")]},
    {500: [(True, "Рука"), (False, "Бровь"),
           (False, "Глаз"), (False, "Шея")]},
    {1_000: [(True, "Каспийское"), (False, "Азовское"),
             (False, "Чёрное"), (False, "Средиземное")]},
    {5_000: [(True, "Бильярдный шар"), (False, "Баскетбольный мяч"), (False, "Апельсин"),
             (False, "Кокосовый орех")]},
    {10_000: [(True, "Гром-камень"), (False, "Дом-камень"), (False, "Гора-камень"),
              (False, "Разрыв-камень")]},
    {50_000: [(True, "Меланхолическая"), (False, "Флегматическая"), (False, "Холерическая"),
              (False, "Сангвиническая")]},
    {100_000: [(True, "«Орден двойного дракона» (Китай)"), (False, "«Ожерелье Нила» (Египет)"),
               (False, "«Крест Грюнвальда» (Польша)"), (False, "«Плайя Хирон» (Куба)")]},
    {200_000: [(True, "Пума"), (False, "Оцелот"),
               (False, "Леопард"), (False, "Пантера")]},
    {500_000: [(True, "Спали"), (False, "Ели"),
               (False, "Ездили верхом"), (False, "Купались")]},
    {1_000_000: [(True, "Кобальт"), (False, "Гафний"),
                 (False, "Бериллий"), (False, "Теллур")]},
]
name_1 = "Звонок другу"
name_2 = "50/50"
name_3 = "Помощь зала"
hints = [name_1, name_2, name_3]
i = 0


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def counter():
    count_1 = 0
    if i > 0:
        count = list(questions[(i + 9)].keys())
        count_1 = count[0]
    return count_1


def getting_money(i):
    if i < 9:
        print("Вы выиграли", str(counter()), "рублей!")


def one_question(i):
    question_dict = questions[(i + 10)]
    value_question = list(question_dict.keys())
    a = question_dict.values()
    b = list(a)
    b_1 = b[0]
    c = list(b_1)
    answ_list = []
    print("Вопрос на " +
          str(value_question[0]) + " рублей:\n" + questions[i])
    print("Варианты ответов:")
    k = 0
    while k < 4:
        q = randint(0, (3 - k))
        answ_var = c.pop(q)
        print(str(k + 1) + ": " + str(answ_var[1]))
        k += 1
        new_answ = list(answ_var)
        answ_list = answ_list + new_answ
    new_answ_list = list(answ_list)
    print("Выберите Ваш вариант ответа: (для выбора подсказки нажмите 5)")
    answ_numb = int(input())
    answ_check = answ_numb * 2 - 2

    def hints_activ_call():
        len_answ_call = len(answ_list)
        call_choice = randrange(1, (len_answ_call-1), 2)
        print("Ваш друг выбрал вариант:", answ_list[call_choice])
        print()

    def hints_activ_hall():
        len_answ_hall = len(answ_list)
        hall_choice = randrange(1, (len_answ_hall-1), 2)
        print("Зал выбрал вариант:", answ_list[hall_choice])
        print()

    def hints_fifty():
        step = 0
        if answ_list[step] == False:
            del (answ_list[0])
            del (answ_list[0])
        else:
            del (answ_list[2])
            del (answ_list[2])
        if answ_list[step] == False:
            del (answ_list[0])
            del (answ_list[0])
        else:
            del (answ_list[2])
            del (answ_list[2])
        one_of_fyfty = answ_list[1:4:2]
        print("Один из правильных вариантов:")
        print(str(one_of_fyfty[0]))
        print(str(one_of_fyfty[1]))
        print()

    if answ_numb == 5:

        def one_step():
            if len(hints) == 0:
                print("Подсказок больше нет!")
                print()
                return
            else:
                print("Выберите подсказку:")
                l = 0
                while l < len(hints):
                    print(str(l + 1) + ": " + str(hints[l]))
                    l += 1
                hint_numb = int(input())
                if hints[hint_numb - 1] == name_1:
                    hints_activ_call()
                if hints[hint_numb - 1] == name_3:
                    hints_activ_hall()
                if hints[hint_numb - 1] == name_2:
                    hints_fifty()
                del hints[(hint_numb - 1)]

        while len(hints) >= 0:
            print(
                "Нажмите:\n 1 - для выбора подсказки\n 2 - продолжить\n 3 - чтобы забрать деньги")
            step_after_hint = int(input())
            if step_after_hint == 1:
                one_step()
            if step_after_hint == 2:
                print("Вопрос на " +
                      str(value_question[0]) + " рублей:\n" + questions[i])
                print("Варианты ответов:")
                print("1:", str(new_answ_list[1]))
                print("2:", str(new_answ_list[3]))
                print("3:", str(new_answ_list[5]))
                print("4:", str(new_answ_list[7]))
                print("Выберите Ваш вариант ответа:")
                answ_numb = int(input())
                answ_check = answ_numb * 2 - 2

                if new_answ_list[answ_check] == True:
                    print("Верно!")
                    print("Вы выиграли " + str(value_question[0]) + " рублей")
                    sleep(2)
                    clear()
                    return True

                elif answ_list[answ_check] == False:
                    print("Ответ неверный. Ваш выигрыш - 0!")
                    return False
            if step_after_hint == 3:
                return "get_money"

    elif answ_list[answ_check] == True:
        print("Верно!")
        print("Вы выиграли " + str(value_question[0]) + " рублей")
        sleep(2)
        clear()

    elif answ_list[answ_check] == False:
        print("Ответ неверный. Ваш выигрыш - 0!")
        return False


while i <= 9:
    result = one_question(i)
    if result == False:
        break
    elif result == "get_money":
        getting_money(i)
        break
    if result == True:
        counter()
    i += 1
