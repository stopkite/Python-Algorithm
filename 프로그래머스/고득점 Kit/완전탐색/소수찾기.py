from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(map(int, numbers))
    all_numbers = get_all_numbers(numbers)
    all_numbers = set(all_numbers)
    for number in all_numbers:
        if is_prime_number(number):
            answer += 1
    return answer


def get_all_numbers(numbers):
    all_numbers = []
    for i in range(1, len(numbers) + 1):
        for v in permutations(numbers, i):
            number = ''.join(list(map(str, v)))
            all_numbers.append(int(number))
    return all_numbers


def is_prime_number(number):
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True
