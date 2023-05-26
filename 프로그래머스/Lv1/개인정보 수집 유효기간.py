def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    today_sum = (today[0] * 28 * 12) + (today[1] * 28) + today[2]

    terms_d = {}
    for i in range(len(terms)):
        terms[i] = terms[i].split(' ')
        terms_d[terms[i][0]] = int(terms[i][1]) * 28

    for i in range(len(privacies)):
        privacies[i] = privacies[i].split(" ")
        privacies[i][0] = privacies[i][0].split('.')

    for i in range(len(privacies)):
        date_sum = (int(privacies[i][0][0]) * 28 * 12) + (int(privacies[i][0][1]) * 28) + int(privacies[i][0][2])
        date_sum += terms_d[privacies[i][1]]

        if today_sum >= date_sum:
            answer.append(i + 1)

    return answer
