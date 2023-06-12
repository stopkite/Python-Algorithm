'''
1. 다음 문자열 만큼 이동한 후 시작할 때는 반복문에 step을 넣어주어 해결한다
ex) for i in range(i, len(s), i)

2. 문제에서 요구하는 것은 길이 자체였기 때문에 len(res)로 길이 자체를 배열 result에 넣어준다

3. 다음 문자열과 비교를 위해 temp를 갱신해준다. (주의! 초기화가 아님)
temp = s[j:i+j]

4. 마지막 조건을 잘 체크하자

5. edge 케이스인 끝 값과 첫 값을 잘 체크하자
'''


def solution(s):
    result = []
    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        temp = s[:i]
        cnt = 1

        res = ''
        for j in range(i, len(s), i):
            if temp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    res += str(cnt) + temp
                else:
                    res += temp
                temp = s[j:j + i]
                cnt = 1

        if cnt != 1:
            res += str(cnt) + temp
        else:
            res += temp

        result.append(len(res))

    return min(result)
