def is_full_memory(memory):
    if len(memory) == 8:
        return True
    return False


def solution(param0, result):
    types = {
        "BOOL": 1,
        "SHORT": 2,
        "FLOAT": 4,
        "INT": 8,
        "LONG": 16
    }

    memory = ''
    memories = []
    for data in param0:
        size = types[data]

        # BOOL
        if size == 1:
            if is_full_memory(memory):
                memories.append(memory)
                memory = ''
            else:
                memory += '#'

        # SHORT, FLOAT
        elif size == 2:
            if is_full_memory(memory):
                memories.append(memory)
                memory = ''

            # 2배수 메모리 할당
            idx = len(memory)
            while idx % 2 != 0:
                memory += '.'

            for _ in range(2):
                memory += '#'

        elif size == 4:
            if is_full_memory(memory):
                memories.append(memory)
                memory = ''

            # 4배수 메모리 할당
            idx = len(memory)
            while idx % 4 != 0:
                memory += '.'

            for _ in range(4):
                memory += '#'

        # INT, LONG
        elif size == 8:
            if is_full_memory(memory):
                memories.append(memory)
                memory = '########'
                memories.append(memory)
            else:
                while len(memory) != 8:
                    memory += '.'
                memories.append(memory)
                memory = "########"
                memories.append(memory)
        else:
            if is_full_memory(memory):
                memories.append(memory)
                memory = '########'
                memories.append(memory)
                memories.append(memory)
            else:
                while len(memory) != 8:
                    memory += '.'
                memories.append(memory)
                memory = "########"
                memories.append(memory)
                memories.append(memory)

    answer = ','.join(memories)

    print(result)

    if len(memories) > 16:
        return "HALT"

    return answer


print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"], "########,########,#.##....,########,########"))
print(solution(["INT", "SHORT", "FLOAT", "INT", "BOOL"], "########,##..####,########,#......."))
print(solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"], "########,#.......,########"))
print(solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"], "HALT"))
