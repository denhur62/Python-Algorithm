def solution(numbers):
    stack = []
    numbers_len = len(numbers)
    answer = [-1] * numbers_len
    for i in range(numbers_len):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer



print(solution([9, 1, 5, 3, 6, 2]))