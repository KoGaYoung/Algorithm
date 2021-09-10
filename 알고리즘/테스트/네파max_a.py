# 2021네이버파이낸셜 하반기 1번(20분)
def solution(S):
    # write your code in Python 3.6
    flag = False
    if 'aaa' in S:
        return -1
    elif S == 'aa':
        return 0
    else:
        origin_S = S
        S = S.replace('a', '')
        s_list = []
        for ch in S:
            s_list.append(ch + 'aa')
        S = ''.join(s_list)
        S = 'aa' + S
        return len(S) - len(origin_S)
print(solution("aabab"))  # aabaabaa
print(solution("dog"))  # aadaaoaagaa
print(solution("aa"))  # 0
print(solution("baaa"))  # -1