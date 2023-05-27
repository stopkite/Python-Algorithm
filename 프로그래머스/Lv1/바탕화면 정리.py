def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])

    lux, luy = n, m
    rdx, rdy = 0, 0

    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                lux = min(i, lux)
                luy = min(j, luy)
                rdx = max(i, rdx)
                rdy = max(j, rdy)

    answer = [lux, luy, rdx + 1, rdy + 1]

    return answer
