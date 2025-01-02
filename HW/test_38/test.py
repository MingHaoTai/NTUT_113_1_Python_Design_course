def getData():
    n, start, end = map(int, input().split())
    rest = map(int, input().split())
    graph = {}
    for i in range(n):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = [a]
        graph[a].append(b)
        graph[b].append(a)
    return start, end, rest, graph

def findShortest(graph : dict, start : int, end : int):
    queue = [(start, [start])]
    visited = []
    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        if current not in visited:
            visited.append(current)
            for i in graph.get(current, []):
                if i not in visited:
                    queue.append((i, path + [i]))
    return None

if __name__ == '__main__':
    start, end, restStop, graph = getData()
    shortest_path = None
    rest = None
    for i in restStop:
        start_to_rest = findShortest(graph, start, i)
        rest_to_end = findShortest(graph, i, end)
        if start_to_rest != None and rest_to_end != None:
            start_to_end = start_to_rest[:-1] + rest_to_end
            if shortest_path == None or len(start_to_end) < len(shortest_path):
                shortest_path = start_to_end
                rest = i
    if shortest_path != None:
        print(rest)
        print(' '.join(map(str, shortest_path)))
    else:
        print('NO')