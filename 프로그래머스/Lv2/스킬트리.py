def solution(skill, skill_trees):
    answer = len(skill_trees)

    temp = []
    for tree in skill_trees:
        for i in range(len(skill)):
            tree = tree.replace(skill[i], str(i))

        res = ''
        for i in range(len(tree)):
            if not tree[i].isalpha():
                res += tree[i]
        temp.append(res)

    print(temp)
    for elem in temp:
        if list(elem) != sorted(elem):
            answer -= 1

    return answer