# 1. 문제를 이해할 때까지 코드 작성을 시작하지 않는다.
# - 문제 이해가 되지 않으면 예시를 통해 규칙을 찾는다
# 2. 도식화를 통해 긴 흐름을 잘게 나눈다.
# 3. 2번을 한 단계씩 찍어서 나중에 오류가 났을 때 멘붕방지

'''
len(memory)를 미리 변수로 선언해주면 while 문을 돌릴 때 루프를 빠져 나올 수가 없다
'''


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

    return answer


print(solution(["INT", "INT", "BOOL", "SHORT", "LONG"], "########,########,#.##....,########,########"))
print(solution(["INT", "SHORT", "FLOAT", "INT", "BOOL"], "########,##..####,########,#......."))
print(solution(["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"], "########,#.......,########"))
print(solution(["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL", "LONG", "SHORT", "LONG", "LONG"], "HALT"))
