'''



'''
def solution(user_times, T):
    # if T == 1:
    #     return 0
    left = []
    for user in user_times:
        if user % T == 0:
            left.append(0)
        else:
            left.append(T-(user % T))
    # left = [T-(user % T) for user in user_times]
    print(left)
    return max(left)


print(solution([20, 40, 65, 100], 30))  # 25
print(solution([20, 40, 65, 100], 1))  # 1
print(solution([10,5,4,7], 2))