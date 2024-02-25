from collections import deque


def solution(m, k):
    m_dict = {}
    for i in range(len(m)):
        ch = m[i]
        if ch not in m_dict:
            m_dict[ch] = deque([i])
        else:
            m_dict[ch].append(i)

    m_list = list(m)

    index = m_dict[k[0]].popleft()
    m_list[index] = m_list[index].upper()

    for i in range(1, len(k)):
        prev_ch = k[i - 1]
        cur_ch = k[i]
        while m_dict[prev_ch] and m_dict[cur_ch][0] < m_dict[prev_ch][0]:
            m_dict[cur_ch].popleft()
        index = m_dict[cur_ch].popleft()
        m_list[index] = m_list[index].upper()

    answer = ''
    for ch in m_list:
        if ch.islower():
            answer += ch

    return answer


solution("kkaxbycyz", "abc")
solution("acbbcdc", "abc")
