"""
1) rank를 n + 1로 초기화하는 이유는 개수 보다 뒤에 선언되는게 최대이기 때문이다.
2) scores가 무조건 입력되는 건 아니라는 조건을 기억하자!
"""

n, s, p = map(int, input().split())

if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    if n == p and scores[-1] >= s:
        print(-1)
    else:
        rank = n + 1
        for i in range(n):
            if scores[i] <= s:
                rank = i + 1
                break
        print(rank)

