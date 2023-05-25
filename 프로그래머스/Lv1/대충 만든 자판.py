def solution(keymap, targets):
    answer = []
    kd = {}

    for key in keymap:
        for i in range(len(key)):
            if key[i] not in kd:
                kd[key[i]] = i + 1
            else:
                if kd[key[i]] > i + 1:
                    kd[key[i]] = i + 1

    for target in targets:
        total = 0
        for i in range(len(target)):
            if target[i] in kd:
                total += kd[target[i]]
            else:
                total = -1
                break
        answer.append(total)

    return answer
