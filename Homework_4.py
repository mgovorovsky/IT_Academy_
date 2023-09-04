from random import randint, randrange
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
quant_hints = len(hints)


def one_question(i):
    question_dict = questions[(i + 10)]
    value_question = list(question_dict.keys())
    a = question_dict.values()
    b = list(a)
    c = b.pop()
    print("Вопрос на " + str(value_question[0]) + " рублей:\n" + questions[i])
    print("Варианты ответов:")
    k = 0
    answ_list = []
    while k < 4:
        q = randint(0, (3 - k))
        answ_var = c.pop(q)
        print(str(k + 1) + ": " + str(answ_var[1]))
        k += 1
        new_answ = list(answ_var)
        answ_list = answ_list + new_answ
    # print(answ_list)  # показывает варианты ответов
    print("Выберите Ваш вариант ответа: (для выбора подскази нажмите 5)")
    answ_numb = int(input())
    answ_check = answ_numb * 2 - 2
    if answ_numb == 5:

        def hints_activ_call():
            len_answ_call = len(answ_list)
            call_choise = randrange(1, (len_answ_call-1), 2)
            print("Ваш друг выбрал вариант:", answ_list[call_choise])

        def hints_activ_hall():
            len_answ_hall = len(answ_list)
            hall_choise = randrange(1, (len_answ_hall-1), 2)
            print("Зал выбрал вариант:", answ_list[hall_choise])

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

        def hints_choise():
            l = 0
            if quant_hints != 0:
                print("Выберите подсказку: ")
                while l < quant_hints:
                    print(str(l + 1) + ": " + str(hints[l]))
                    l += 1
                hint_numb = int(input())

                if hints[hint_numb] == name_1:
                    hints_activ_call()
                if hints[hint_numb] == name_3:
                    hints_activ_hall()
                if hints[hint_numb] == name_2:
                    hints_fifty()
                del hints[(hint_numb - 1)]
                # print(hints)  # смотрим, что осталось из подсказок
            else:
                print("Подсказок больше нет!")
    elif answ_list[answ_check] == False and answ_numb != 5:
        print("Ответ неверный. Ваш выигрыш - 0!")
    else:
        print("Верно!")


one_question(9)
