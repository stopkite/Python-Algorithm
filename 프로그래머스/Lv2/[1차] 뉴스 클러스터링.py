def solution(str1, str2):
    sd1 = get_pair_dict(str1)
    sd2 = get_pair_dict(str2)

    ul, al = get_set(sd1, sd2)
    answer = get_jacard_value(ul, al)

    return answer


# 1.글자쌍 딕셔너리 구하기
def get_pair_dict(s):
    s = s.upper()
    dict = {}
    for i in range(0, len(s) - 1):
        if not s[i].isalpha() or not s[i + 1].isalpha():
            continue
        w = s[i] + s[i + 1]

        if w not in dict:
            dict[w] = 1
        else:
            dict[w] += 1
    return dict


# 2.교집합, 합집합 길이 구하기
def get_set(d1, d2):
    same_list = []
    for ch in d1.keys():
        if ch in d1 and ch in d2:
            same_list.append(ch)

    union_arr = []
    add_arr = []
    for key, value in d1.items():
        if key in same_list:
            union_arr.append(min(d1[key], d2[key]))
        else:
            add_arr.append(value)

    for key, value in d2.items():
        if key in same_list:
            add_arr.append(max(d1[key], d2[key]))
        else:
            add_arr.append(value)

    union_len = sum(union_arr)
    add_len = sum(add_arr)

    return union_len, add_len


# 3.유사도 구하기
def get_jacard_value(ul, al):
    if ul == 0 and al == 0:
        answer = 1
    else:
        answer = ul / al

    return int(answer * 65536)
