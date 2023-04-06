n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

arr = list(set(arr))  # 중복 제거

arr.sort()  # 사전순으로 정렬
arr.sort(key=len)  # 길이 짧은 순으로 정렬

for elem in arr:
    print(elem)
