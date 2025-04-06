A, B = map(int, input().split())

def bfs(start, end):
    queue = [(start, 0)]
    # visited = [False] * (B + 1)

    while queue:
        current = queue.pop(0)
        current, count = current[0], current[1]
        # if (current < A) or (current > B) or visited[current]:
        if (current < A) or (current > B):
            continue
        
        count += 1
        # visited[current] = True

        if current == end:
            return count
        elif current > end:
            continue

        queue.append((current * 2, count))
        queue.append((current * 10 + 1, count))
        
    return -1
        
result = bfs(A, B)
print(result)


# print()
# # print counts and break every 10
# for i in range(len(counts)):
#     if i % 10 == 0 and i != 0:
#         print()
#     print(counts[i], end=" ")
# print()