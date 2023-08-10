"""
지문을 이해하지 못 해 is_beautiful 함수의 로직을 생각해내는 것이 어려웠다.
답지를 봤으나 범위를 i + seq[i] - 1 로 표현하는 것 역시 생소했던 문제이다.
다시 봐야할 독특한 풀이법이다.
"""

n = int(input())
ans = 0
seq = list()


def is_beautiful_num():
    i = 0
    while i < n:
        if i + seq[i] - 1 >= n:
            return False
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False

        i += seq[i]

    return True


def count_beautiful_seq(cnt):
    global ans

    if cnt == n:
        if is_beautiful_num():
            ans += 1
        return

    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(i)
        seq.pop()


count_beautiful_seq(0)
print(ans)
