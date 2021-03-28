from collections import Counter


def solution(genres, plays):
    arr = []
    length = len(set(genres))
    cl = [[]*length for _ in range(length)]
    g_idx = 0
    for idx, val in enumerate(genres):
        if val not in arr:
            arr.append(val)
            cl[g_idx].append((plays[idx], idx))
            g_idx += 1
        else:
            cl[arr.index(val)].append((plays[idx], idx))
    print(cl)
    for a in cl:
        count = 0
        for b in a:
            count += b[0]
        a.append(count)
    c = sorted(cl, key=lambda x: -x[-1])
    print("cl", c)
    d = []
    for i in c:
        i.remove(i[-1])
        d.append(sorted(i, key=lambda x: -x[0]))
    print(d)

    answer = []
    for i in d:
        for j in i[:2]:
            answer.append(j[1])

    return answer


genres = ["classic", "pop", "classic", "pop", "classic", "classic"]
plays = [400, 600, 150, 600, 500, 500]

print(solution(genres, plays))
