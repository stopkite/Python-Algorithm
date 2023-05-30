dict = {}

dict['b'] = 1
dict['a'] = 1

print(dict)

dict2 = {}
dict2['a'] = 1
dict2['b'] = 1

print(dict2)

if dict == dict2:
    print("순서가 달라도 안에 내용이 같으면 같은걸로 취급된다")