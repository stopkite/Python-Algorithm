"""
right 랑 left 미는 것에 있어서 for문을 작성하기 힘들었다.
위, 아래로 미는 것까지 연습할 필요를 느꼈다.
"""

n, t = map(int, input().split())
a1 = list(input().split())
a2 = list(input().split())[::-1]

for _ in range(t):
    a1_e = a1[n - 1]
    a2_s = a2[0]

    # 'right' 이동
    for i in range(n - 1, 0, -1):
        a1[i] = a1[i - 1]

    # 'left' 이동
    for i in range(n - 1):
        a2[i] = a2[i + 1]

    # 'down' 이동
    a2[n - 1] = a1_e

    # 'up' 이동
    a1[0] = a2_s

for elem in a1:
    print(elem, end=" ")

print()

for elem in a2[::-1]:
    print(elem, end=" ")