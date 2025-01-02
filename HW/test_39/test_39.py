def getData():
    n, start = map(int, input().split())
    graph = {}
    holeGold = {}
    for i in range(n):
        a, gold, b, c = map(int, input().split()) 
        graph[a] = []
        graph[a].append(b)
        graph[a].append(c)
        holeGold[a] = gold
    return start, graph, holeGold

def allPaths_dfs(start : int, graph : dict,visited : list, path : list, all_paths : list):
    visited.append(start)
    path.append(start)
    if (graph[start][0] == 0 and graph[start][1] == 0) or (graph[start][0] in visited and graph[start][1] in visited):
        all_paths.append(path[0:])  # copy a new list of path into all_paths, so need to add [0:]
    else:
        for i in graph.get(start, []):
            if i not in visited:
                allPaths_dfs(i, graph, visited, path, all_paths)
    path.pop()
    visited.remove(start)

def findMostGold(path : list, holeGold : dict):
    gold = 0
    for i in path:
        gold += holeGold[i]
    return gold

if __name__ == '__main__':
    start, graph, holeGold = getData()
    all_paths = []
    allPaths_dfs(start, graph, [], [], all_paths)
    mostGold = 0
    for i in all_paths:
        gold = findMostGold(i, holeGold)
        if gold > mostGold:
            mostGold = gold
    print(mostGold)
    