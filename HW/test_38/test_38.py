# 2024-12-28
def getData():
    n, start, end = map(int, input().split())  # road amounts, start stop, end stop
    restStop = map(int, input().split())    # rest stop
    graph = {}  # every stop connect
    for i in range(n):  # every road
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return start, end, restStop, graph

def findShortest(start, end, graph):
    queue = [(start, [start])]  # the stack (next_start_stop, path)
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
    shortestRest = None
    shortestEnd = None
    shortest = None
    allPath = None
    Stop = None
    for rest in restStop:
        shortestRest = findShortest(start, rest, graph)
        shortestEnd = findShortest(rest, end, graph)
        if shortestEnd != None and shortestRest != None:
            all_path = shortestRest[:-1] + shortestEnd
            if shortest == None or len(all_path) < len(shortest):
                shortest = all_path
                Stop = rest
    if shortest != None:
        print(Stop)
        print(' '.join(map(str, shortest)))
    else:
        print('NO')