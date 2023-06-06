def solution():
    s = input()

    if not check_error(s):
        return "Error!"

    lang = check_lang_type(s)
    if lang == "java":
        answer = java_to_cpp(s)
    else:
        answer = cpp_to_java(s)

    return answer


# 에러 체크
def check_error(s):
    for i in range(len(s) - 1):
        # 기호가 연속으로 쓰일 경우(ja__va, @#$!@)
        if not s[i].isalpha() and not s[i + 1].isalpha():
            return False

    # 첫 문자 -> 숫자 or 기호(1ava, _ava)
    if not s[0].isalpha():
        return False

    # 첫 문자, 두 번째 문자 -> 대문자, 대문자 일 경우 (JJava)
    if s[0].isupper() and s[1].isupper():
        return False

    # 첫문자 -> 대문자
    if s[0].isupper():
        return False

    # 띄어 쓰기 있으면 return
    if ' ' in s:
        return False

    # 자바, c++ 혼용 (jJ_va)
    if not s.islower():
        for i in range(len(s)):
            if s[i] == '_':
                return False

    # 맨 끝에 '_'가 붙으면 (asaf_)
    if s[-1] == "_":
        return False

    return True


# 언어 체크
def check_lang_type(s):
    if "_" in s:
        return "cpp"
    else:
        return "java"


def cpp_to_java(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '_':
            s[i + 1] = s[i + 1].upper()
    s = ''.join(s)
    answer = s.replace("_", "")
    return answer


def java_to_cpp(s):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            answer += '_'
            answer += s[i].lower()
        else:
            answer += s[i]
    return answer


print(solution())
