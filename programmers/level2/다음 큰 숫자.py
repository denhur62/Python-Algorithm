
def solution(numbers):
    binary_numbers= bin(numbers)
    count=str(binary_numbers[2:]).count('1')
    for i in range(numbers+1,1000000):
        if count == str(bin(i)[2:]).count('1'):
            return i


print(solution(78))