n = int(input())
people = {}

for _ in range(n):
    person, state = input().split()
    if state == 'enter':
        people[person] = 1
    else:
        people[person] = 0

answer = []
for k,v in people.items():
    if v == 1:
        answer.append(k)

answer.sort()
for p in answer[::-1]:
    print(p)
