import os
from sys import argv


def get_page_number_list() -> list[int]:
    l = list(map((lambda x: x.split()[0]), os.listdir()))
    ll = []
    for i in l:
        if not i.isdigit():
            i = i[:i.find('.')]
        if i.isdigit():
            ll.append(int(i))
    return ll


def get_next_page_number() -> int:
    return max(get_page_number_list()+[0,]) + 1


def create_next_page(flag: bool = False) -> None:
    temp = get_next_page_number()

    if flag:
        os.mkdir(f"{temp}")
        # print(f"Gen dir {temp}")
    else:
        with open(f"{temp}.py", "w") as f:
            pass
        # print(f"Gen py {temp}.py")


def display_commands_list(*arg) -> None:
    global Comands_list
    for i in Comands_list.keys():
        print(f'{i}: {Comands_list[i][1]}')


def f0(*arg) -> None:
    quit()


def f1(*arg) -> None:
    if arg:
        for _ in range(abs(int(arg[0]))):
            create_next_page(False)
    else:
        create_next_page(False)


def f2(*arg) -> None:
    if arg:
        for _ in range(abs(int(arg[0]))):
            create_next_page(True)
    else:
        create_next_page(True)


def main():
    global Comands_list
    display_commands_list()

    while 1:
        is_correct = False
        while not is_correct:
            inp = input("Введите Команду> ").split()
            if inp != []:
                is_correct = inp[0] in Comands_list

        Comands_list[inp.pop(0)][0](*inp)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    Comands_list = {"0": [f0, "Выход"],
                    "1": [display_commands_list, 'Спрафка'],
                    "2": [f1, 'Добавить Файл; N'],
                    "3": [f2, 'Добавить Папку; N']}

    if len(argv) > 1:
        for i in argv[1:]:
            if i in Comands_list.keys():
                Comands_list[i][0]()
    else:
        main()
