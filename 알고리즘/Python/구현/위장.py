
def solution(clothes):
    wear = {}
    for item in clothes:
        if item[1] not in wear:
            wear[item[1]] = [item[0]]
        else:
            wear[item[1]].append(item[0])
    a = 1
    for item in wear:
       a *= len(wear[item])+1
    return a-1


print(solution([['A', 'head'],['B', 'head'], ['C', 'eye'], ['D', 'eye'], ['E', 'mouse']]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))