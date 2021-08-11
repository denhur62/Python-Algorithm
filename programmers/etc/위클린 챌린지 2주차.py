
def solution(scores):
    scores = list(map(list, zip(*scores)))
    answer = ''
    cnt = 0
    for i in scores:
        score_sum = sum(i)
        length = len(scores)
        j = []
        for k in range(length):
            j.append(scores[k][cnt])
        if scores[cnt][cnt] == max(j) or scores[cnt][cnt] == min(j):
            if len(set(j)) == len(j):
                score_sum -= scores[cnt][cnt]
                length -= 1
        score_sum /= length
        if score_sum >= 90:
            answer += 'A'
        elif 80 <= score_sum < 90:
            answer += 'B'
        elif 70 <= score_sum < 80:
            answer += 'C'
        elif 50 <= score_sum < 70:
            answer += 'D'
        else:
            answer += 'F'
        cnt += 1
    return answer


scores = [[50, 90], [50, 87]]
print(solution(scores))
