n = 3
answer = []


def show_answer():
    for elem in answer:
        print(elem, end=" ")
    print()


def choose(cur_num):
    if cur_num == n + 1:
        show_answer()
        return

    answer.append(0)
    choose(cur_num + 1)
    answer.pop()

    answer.append(1)
    choose(cur_num + 1)
    answer.pop()

    return

choose(1)