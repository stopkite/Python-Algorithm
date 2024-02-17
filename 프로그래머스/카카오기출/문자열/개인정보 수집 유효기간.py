def solution(today, terms, privacies):
    answer = []
    year, month, day = map(int, today.split("."))

    # 총일수 = (year x 365) + (month ×  28) + day
    total_today = (year * 28 * 12) + (month * 28) + day

    # 유효기간 역시 month(=달) 단위로 주어졌기때문에 x28을 해준다
    terms_dict = {}
    for term in terms:
        type, term_month = term.split()
        terms_dict[type] = int(term_month) * 28

    #  현재날짜와 기준날짜를 비교해서 둘을 뺀값이 유효기간 보다 크면 유효기간을 넘긴 상태이다
    for idx, p in enumerate(privacies):
        saved_date, type = p.split()
        year, month, day = map(int, saved_date.split("."))
        total_saved_date = (year * 28 * 12) + (month * 28) + day

        if total_today - total_saved_date >= terms_dict[type]:
            answer.append(idx + 1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
