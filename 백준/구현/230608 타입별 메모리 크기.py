def assign_data(memory, data_size):
    while len(memory) % data_size != 0:
        memory += '.'
    for _ in range(data_size):
        memory += '#'
    return memory


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

        if len(memory) == 8:
            memories.append(memory)
            memory = ''

        if size == 1:
            memory += '#'
        elif size == 2:
            while len(memory) % 2 != 0:
                memory += '.'
            memory += '#' * 2
        elif size == 4:
            while len(memory) % 4 != 0:
                memory += '.'
            memory += '#' * 4
        else:
            if len(memory) != 0:
                while len(memory) % 8 != 0:
                    memory += '.'
                memories.append(memory)
            memory = '#' * 8

            if size == 16:
                memories.append(memory)
                memory = '#' * 8
                memories.append(memory)
                memory = ''

    # 마지막 메모리 값 체크
    if len(memory) != 0:
        while len(memory) != 8:
            memory += '.'
        memories.append(memory)

    if len(memories) > 16:
        answer = "HALT"
    else:
        answer = ','.join(memories)

    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print(result)
    return answer


print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"], "########,########,#.##....,########,########"))
print(solution(["INT", "SHORT", "FLOAT", "INT", "BOOL"], "########,##..####,########,#......."))
print(solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"], "########,#.......,########"))
print(solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"], "HALT"))
