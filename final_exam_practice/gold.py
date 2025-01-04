def getData():
    n, start = map(int, input().split())
    graph = {}
    gold = {}
    for i in range(n):
        data = list(map(int, input().split()))
        if len(data) > 2:
            graph[data[0]] = []
            for i in range(2, len(data)):
                graph[data[0]].append(data[i])
        else:
            graph[data[0]] = None
        gold[data[0]] = data[1]
    return start, graph, gold

def dfs(start : int, graph : dict, visited : list, path : list, allPaths : list):
    path.append(start)
    visited.append(start)
    if graph[start] == None:
        allPaths.append(path[0:])
    else:
        for i in range(len(graph[start])):
            if graph[start][i] not in visited:
                break
            elif graph[start][i] in visited and i == len(graph[start])-1:
                allPaths.append(path[0:])
                path.pop()
                visited.remove(start)
                return
        
        for i in graph.get(start, []):
            if i not in visited:
                dfs(i, graph, visited, path, allPaths)

    path.pop()
    visited.remove(start)

def findGold(path : list, gold : dict):
    amount = 0
    for i in path:
        amount += gold[i]
    return amount
    
if __name__ == '__main__':
    start, graph, gold = getData()
    # print(gold)
    allPaths = []
    dfs(start, graph, [], [], allPaths)
    # print(allPaths)
    amount = 0
    for i in allPaths:
        if findGold(i, gold) > amount:
            amount = findGold(i, gold)
    print(amount)