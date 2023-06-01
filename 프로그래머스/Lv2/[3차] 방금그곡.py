'''
지문을 똑바로 읽자....
문제에서 요구하는 바를 확실히 체크하자 ...
멜로디가 긴게 아니라 재생시간이 긴 것이 정답
'''

def solution(m, musicinfos):
    answer = ''
    cur_time = 0

    sdic1 = {'C#': '0', 'D#': '1', 'F#': '2', 'G#': '3', 'A#': '4'}

    m = ''.join(get_mellodi_list(sdic1, m))

    for mi in musicinfos:
        mi = mi.split(",")
        st, ed = mi[0].split(":"), mi[1].split(":")
        title, song = mi[2], mi[3]

        # 재생 시간
        time = (int(ed[0]) * 60) + int(ed[1]) - (int(st[0]) * 60) - int(st[1])

        # 멜로디
        list_song = get_mellodi_list(sdic1, song)
        repeat = time // len(list_song)
        ed = time % len(list_song)
        music = ''.join((list_song * repeat)) + ''.join(list_song[:ed])

        if m in music:
            if time > cur_time:
                cur_time = time
                answer = title

    if cur_time == 0:
        answer = "(None)"

    return answer


def get_mellodi_list(sdic1, m):
    for s, num in sdic1.items():
        if s in m:
            m = m.replace(s, num)

    list_m = []
    for i in range(len(m)):
        list_m.append(m[i])
    return list_m
