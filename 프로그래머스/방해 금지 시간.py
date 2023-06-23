def solution(noti_time, do_not_disturb, result):
    answer = ""

    time = {}
    for t in range((24 * 60) + 1):
        time[t] = 0

    for d in do_not_disturb:
        st, ed = d.split("~")
        ed_h, ed_m = ed.split(":")
        st_h, st_m = st.split(":")

        # 시간 차 계산
        ed_total = (int(ed_h) * 60) + int(ed_m)
        st_total = (int(st_h) * 60) + int(st_m)

        # 방해 시간 저장
        if ed_total < st_total:  # 24시간이 넘을 때
            for t in range(ed_total):
                time[t] = 1
            for t in range(st_total, (24 * 60) + 1):
                time[t] = 1
        else:
            for t in range(st_total, ed_total):
                time[t] = 1

    # 알림 시간 구하기
    nh, nm = noti_time.split(":")
    noti_total = (int(nh) * 60) + int(nm)

    # 방해시간 포함 x
    if time[noti_total] != 1:
        answer = noti_time
    else:  # 방해시간 포함 o
        total_time = 0
        first_t = 0

        # 최초 시간 저장
        for t in range((24 * 60) + 1):
            if time[t] == 1:
                first_t = t
                break

        # 최근 시간 저장
        for t in range(first_t + 1, (24 * 60) + 1):
            if time[t] == 0:
                total_time = t
                break

        # 알림 불가능
        if total_time == 0:
            answer = "impossible"
        else:
            # 단위 환산
            h = total_time // 60
            m = total_time % 60

            # 자릿수 맞추기
            h = str(h).zfill(2)
            m = str(m).zfill(2)

            answer = h + ":" + m

    if answer == result:
        return "통과"
    else:
        return "실패"


print(solution("23:00", ["22:30~23:40", "23:05~00:45"], "00:45"))
print(solution("09:55", ["09:55~13:25", "13:25~14:01"], "14:01"))
print(solution("00:00", ["11:00~01:00", "23:00~13:00"], "impossible"))
print(solution("09:55", ["13:25~14:01", "09:56~13:25", "20:08~20:15"], "09:55"))
print(solution("23:59", ["00:00~23:59", "11:35~23:59"], "23:59"))
