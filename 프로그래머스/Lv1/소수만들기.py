from itertools import combinations


def solution(nums):
    answer = 0
    checkNumList = getCheckNumList(nums)
    for number in checkNumList:
        if isPrimeNumber(number) == True:
            answer += 1
    return answer


def getCheckNumList(nums):
    checkNumList = []
    for a, b, c in combinations(nums, 3):
        checkNumList.append(a + b + c)
    return checkNumList


def isPrimeNumber(num):
    m = int(num ** 0.5)
    for i in range(2, m + 1):
        if num % i == 0:
            return False
    return True