from itertools import product, combinations

def solution(clothes):
    lookbook = []
    wear = {}
    for item in clothes:
        if item[1] not in wear:
            wear[item[1]] = [item[0]]
            lookbook.append(item[0])
        else:
            wear[item[1]].append(item[0])
            lookbook.append(item[0])

    keys = wear.keys()
    # wear 한 종류 인 경우
    if len(keys) == 1:
        pass
    else:  # wear 종류 이상일 경우
        comb_keys = []
        for i in range(2, len(keys)+1):
            comb_keys.extend(combinations(keys, i))
        for k in comb_keys:
            if len(k) == 2:
                a = list(product(wear[k[0]], wear[k[1]]))
            elif len(k) == 3:
                a = list(product(wear[k[0]], wear[k[1]], wear[k[2]]))
            elif len(k) == 4:
                a = list(product(wear[k[0]], wear[k[1]], wear[k[2], wear[k[3]]]))

            a = [list(i) for i in a]
            for item in a:
                item.sort()
                lookbook.append(' '.join(item))
        lookbook = set(lookbook)
        lookbook = list(lookbook)
    return len(lookbook)


print(solution([['A', 'head'],['B', 'head'], ['C', 'eye'], ['D', 'eye'], ['E', 'mouse']]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))