def solution(participant, completion):
    p = set(participant)
    c = set(completion)
    if len(p-c) > 0:
        return list(p-c)[0]
    else:
        for player in completion:
            if participant.count(player) > completion.count(player):
                return player