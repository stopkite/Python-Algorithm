import sys

trees = {}

total_cnt = 0
while True:
    tree = sys.stdin.readline().strip()
    if tree == '':
        break
    total_cnt += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

sort_trees = dict(sorted(trees.items()))
for k, v in sort_trees.items():
    print(f"{k} {(v / total_cnt) * 100:.4f}")
