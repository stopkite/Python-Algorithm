def solution(park, routes):
    s = [0, 0]
    p = [[True for _ in range(len(park[0]))] for _ in range(len(park))]

    max_row = len(park)-1  # 가로
    max_col = len(park[0])-1  # 세로

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                s = [i, j]
            elif park[i][j] == 'X':
                p[i][j] = False

    cur_pos = s
    for r in routes:
        opp = r.split()[0]
        n = int(r.split()[1])

        i = cur_pos[0]
        j = cur_pos[1]

        if opp == 'W':
            flag = True
            for m in range(1, n + 1):
                if j - m < 0:
                    flag = False
                    break
                if p[i][j - m] == False:
                    flag = False
                    break
            if flag:
                cur_pos[1] = j - n
        elif opp == 'E':
            flag = True
            for m in range(1, n + 1):
                flag = True
                if j + m > max_col:
                    flag = False
                    break
                if p[i][j + m] == False:
                    flag = False
                    break
            if flag:
                cur_pos[1] = j + n
        elif opp == 'N':
            flag = True
            for m in range(1, n + 1):
                flag = True
                if i - m < 0:
                    flag = False
                    break
                if p[i - m][j] == False:
                    flag = False
                    break
            if flag:
                cur_pos[0] = i - n
        else:
            flag = True
            for m in range(1, n + 1):
                flag = True
                if i + m > max_row:
                    flag = False
                    break
                if p[i + m][j] == False:
                    flag = False
                    break
            if flag:
                cur_pos[0] = i + n

    return cur_pos
