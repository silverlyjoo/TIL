L = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
result = []

# def bfs(start, L, result):
#     visited = [0] * len(L)
#     queue = []
#     queue.append(start)
#     while queue:
#         end = queue.pop(0)
#         if not visited[end]:
#             visited[end] = True
#             result.append(end)
#         for i in L[end]:
#             if not visited[i]:
#                 queue.append(i)
#     return result
#
# print(*bfs(1,L, result))


def bfs(start, L, result):
    visited = [0] * len(L)
    queue = []
    queue.append(start)
    while queue:
        end = queue.pop(0)
        if not visited[end]:
            visited[end] = True
            result.append(end)
        for i in L[end]:
            if not visited[i]:
                queue.append(i)
    return result

print(*bfs(1,L, result))