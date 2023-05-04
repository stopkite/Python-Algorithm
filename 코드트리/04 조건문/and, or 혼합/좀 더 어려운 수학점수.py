# 수학 높은 사람 먼저 출력
# 수학 점수 같으면 -> 영어 점수 높은 사람 출력
arr = input().split()
a_math, a_eng = int(arr[0]), int(arr[1])

arr = input().split()
b_math, b_eng = int(arr[0]), int(arr[1])

if a_math > b_math or (a_math == b_math and a_eng > b_eng):
    print("A")
else:
    print("B")