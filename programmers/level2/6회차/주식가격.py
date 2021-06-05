
def solution(prices):
    prices.reverse()
    answer = []
    stack = []
    j = 0
    for i in prices:
        print(stack)
        while stack and prices[stack[-1]] >= i:
            stack.pop()
        if not stack:
            answer.append(j)
        else:
            answer.append(j-stack[-1])
        stack.append(j)
        j += 1
    answer.reverse()
    return answer


# prices=[3,2,3,2,1]
prices = [1, 2, 3, 2, 3]

prices1 = [1, 2, 3, 2, 3, 1]
print(solution(prices))
