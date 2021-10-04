def solution(s):
    '''
    s를 만들 숭 있는 반복자찾기
    반복자들(repeator) 중 반복하여 s를 만족하면서 길이가 가장 짧은 요소의 길이 리턴

    repeator 전제조건
    1) len(s) % repeator == 0
    2) repteator를 len 단위로 끊어서 모든 요소가 repeator와 일치하지않는지

    단, 모든 repeator가 일치하지않으면 len(s)가 리턴된다 '''
    repeator = {}
    for i in range(1, len(s)+1):
        if len(s) % i == 0:
            repeator[s[:i]] = 0

    answer = []
    for item in repeator.keys():
        repeator_check = True
        for i in range(len(item), len(s) + len(item), len(item)):
            if s[i-len(item):i] != item:
                repeator_check = False
        if repeator_check:
            answer.append(len(item))
    return min(answer)