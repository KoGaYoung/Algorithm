def solution(numbers):
    sum = 0
    for item in range(0, 10):
        if item not in numbers:
            sum += item

    return sum
print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))