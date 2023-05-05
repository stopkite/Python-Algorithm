def solution(a, b):
    months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
              6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    days = {3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU", 1: "FRI", 2: "SAT"}

    total_day = 0
    for month, day in months.items():
        if month == a:
            break

        total_day += day

    total_day += b

    result = days[total_day % 7]
    print(total_day % 7)

    return result