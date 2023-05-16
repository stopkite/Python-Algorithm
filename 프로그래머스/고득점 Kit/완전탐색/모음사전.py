from itertools import product

def solution(word):
    a = ["A", "E", "I", "O", "U"]
    dic = []
    for i in range(1, 6):
        tuple_w = list(product(a, repeat=i))
        for w in tuple_w:
            dic.append(''.join(map(str, w)))

    dic.sort()
    answer = dic.index(word) + 1
    return answer