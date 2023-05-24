def solution(players, callings):
    rank = {}

    for i in range(len(players)):
        rank[players[i]] = i

    for call in callings:
        cur_idx = rank[call]
        front_idx = rank[call] - 1
        front_person = players[front_idx]

        rank[front_person] += 1
        rank[call] -= 1

        players[cur_idx] = front_person
        players[front_idx] = call

    return players