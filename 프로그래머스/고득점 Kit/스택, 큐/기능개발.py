from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        cnt = 0
        for d in range(1, 100):  # p[0] 기능 완료 날짜 구하기
            if progresses[0] + (speeds[0] * d) >= 100:
                day = d
                break

        for i in range(len(progresses)):  # 완수율 갱신
            progresses[i] = progresses[i] + (speeds[i] * day)

        for i in range(len(progresses)):  # 완료 작업 개수
            if progresses[0] >= 100:
                cnt += 1
                if len(progresses) == 1:
                    answer.append(cnt)
                progresses.popleft()
                speeds.popleft()
            else:
                answer.append(cnt)
                break

    return answer