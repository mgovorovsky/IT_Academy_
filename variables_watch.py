from colorama import Fore

item_1 = "**"
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

delim_zero = [[space, item_1, space],
              [space, space, space],
              [space, space, space],
              [space, space, space],
              [space, space, space]]

delim_one = [[space, space, space],
             [space, item_1, space],
             [space, space, space],
             [space, space, space],
             [space, space, space]]

delim_two = [[space, space, space],
             [space, space, space],
             [space, item_1, space],
             [space, space, space],
             [space, space, space]]

delim_three = [[space, space, space],
               [space, space, space],
               [space, space, space],
               [space, item_1, space],
               [space, space, space]]

delim_four = [[space, space, space],
              [space, space, space],
              [space, space, space],
              [space, space, space],
              [space, item_1, space]]


space_1 = ["   "]

numbers_dictionary = [zero, one, two, three,
                      four, five, six, seven, eight, nine]

delimiters_dictionary = [delim_zero, delim_one, delim_two, delim_three,
                         delim_four, delim_three, delim_two, delim_one]


rows_number = len(zero)

color = [Fore.RED, Fore.BLACK, Fore.GREEN,
         Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE, Fore.BLUE]
