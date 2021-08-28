# 0과 1끼리 합쳐서 삭제
def solution(s):
    match = {'0' : '1', '1':'0'}
    list = []
    answer = True
    for val in s:
        list.append(val)
        if not len(list):
            return 0
        top = list.pop()
        if match[val] != top:
            answer = False
            break
    return len(list)


print(solution("1011"))
print(solution("0110011"))
print(solution("000111"))