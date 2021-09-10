def backtracking(cards_array, word):
    if len(cards_array) < word:
        return 0
    else:
        # backtracking(row + 1, m_word + m[row][i])
        pass


def solution(word, cards):
    # 백 트래킹
    # 비선형으로 구조화한 다음, 가능한 모든 상태를 깊이 우선
    cards_array = []
    for i in cards:
        temp = []
        for ch in i:
            temp.append(ch)
        cards_array.append(temp)
    answer = 0
    # answer = backtracking(cards_array, word)

    return answer



print(solution('APPLE', ["LLZKE", "LCXEA","CVPPS","EAVSR","FXPFP"]))
print(solution('BAB', ["ZZBZ", "BAZB","XBXB","XBAX"]))
print(solution('BABXZ', ["ZZBZ", "BAZB","XBXB","XBAX"]))