def acmTeam(topic):
    # Write your code here
    scores = []
    for i in range(n - 1):
        for j in range (i + 1, n):
            topic_count = 0
            for num in range(m):
                if topic[i][num] == '1' or topic[j][num] == '1':
                    topic_count += 1
            scores.append(topic_count)

    return [max(scores), scores.count(max(scores))]
