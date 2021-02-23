str = input()

index = 0
number = []
operator = []
for idx, val in enumerate(str):
    if idx == len(str)-1:
        number += [str[index:idx+1]]
    if val == '-' or val == '+':
        operator += val
        number += [str[index:idx]]
        index = idx+1
number = list(map(int, number))
while operator:
    i = 0
    answer = 0
    while '+' in operator:
        if operator[i] == '+':
            number[i] = number[i]+number[i+1]
            del number[i+1]
            del operator[i]
        else:
            i += 1
    i = 0
    while '-' in operator:
        if operator[i] == '-':
            number[i] = number[i]-number[i+1]
            del number[i+1]
            del operator[i]
        else:
            i += 1
print(number[0])
