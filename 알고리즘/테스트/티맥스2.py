def solution(s):
    repeators = []
    for i in range(2, len(s)+1):
        re = s[0:i]
        if len(s) % 2 == len(re) % 2:
            if len(s) % len(re) == 0:
                repeators.append(re)

    len_re = []
    for re in repeators:
        split_s_by_re = [s[i:i+len(re)] for i in range(0, len(s), len(re))]
        all_repeat = True
        for split_s in split_s_by_re:
            if re != split_s:
                all_repeat = False
        if all_repeat:
            len_re.append(len(re))

    return min(len_re)

print(solution('abababab'))  # ab = 2
print(solution('abcabcabd'))  # abcabcabd = 9