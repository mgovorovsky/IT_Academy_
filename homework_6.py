import helpers_watch
from variables_watch import rows_number, delimiters_dictionary


def main():
    n = 0
    while True:
        pass
        helpers_watch.clear()
        [h1, h2, m1, m2, s1, s2] = helpers_watch.get_current_time()
        helpers_watch.print_time(h1, h2, m1, m2, s1, s2, n)
        helpers_watch.time.sleep(1)
        n += 1


if __name__ == "__main__":
    main()
