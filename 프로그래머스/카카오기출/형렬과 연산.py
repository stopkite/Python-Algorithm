from collections import deque


def solution(rc, operations):
    col, row = len(rc), len(rc[0])

    def rotate(rc):
        # 첫째 줄
        d1 = deque(rc[0])
        d1.rotate()

        # 오른쪽 줄
        d2 = deque([row[-1] for row in rc])
        d2.rotate()
        d2[0] = d1[-1]

        # 맨아래 줄
        d3 = deque(rc[col - 1])
        d3.append(d2[-1])
        d3.popleft()

        # 왼쪽 줄
        d4 = deque([row[0] for row in rc])
        d4.append(d3[0])
        d4.popleft()

        d1[0] = d4[0]

        rc[0] = list(d1)  # 첫째 줄
        for i in range(len(rc)):  # 오른쪽 줄
            rc[i][-1] = d2[i]

        rc[col - 1] = list(d3)  # 맨아래 줄

        for i in range(len(rc)):  # 왼쪽 줄
            rc[i][0] = d4[i]

    def shift_row(rc):
        for i in range(col - 1, 0, -1):
            temp = rc[i]
            rc[i] = rc[i - 1]
            rc[i - 1] = temp

            # rc[i], rc[i - 1] = rc[i - 1], rc[i]

    for op in operations:
        if op == "Rotate":
            rotate(rc)
        else:
            shift_row(rc)
    return rc


# solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["ShiftRow"])
solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate"])
