def getData():
    n, start, end = map(int, input().split())
    rest_data = list(map(int, input().split()))
    graph = {}
    length_data = {}
    for i in range(n):
        a, b, length = map(int, input().split())
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
        twoPoints = sorted([a, b])
        length_data[str(twoPoints[0])+str(twoPoints[1])] = length
    return start, end, rest_data, graph, length_data

def getAllPaths_dfs(start, end, graph, path, visited, all_paths):
    flag = False    # If the start's neighbors all visited, the flag will be False
    path.append(start)
    visited.append(start)
    if start == end:
        all_paths.append(path[0:])
    else:
        for i in graph[start]:
            if i not in visited:
                flag = True # There have some neighbors of start not in visited
                break
        if flag == True:
            for i in graph.get(start, []):
                if i not in visited:
                    getAllPaths_dfs(i, end, graph, path, visited, all_paths)
    path.pop()
    visited.remove(start)

def getLength(path, length_data):
    length = 0
    for i in range(0, len(path)-1):
        twoPoints = sorted([path[i], path[i+1]])
        length += length_data[str(twoPoints[0])+str(twoPoints[1])]
    return length

def output1(all_paths, rest_data, length_data):
    all_paths = sorted(all_paths, key=lambda x : len(x))
    visited_rest = []
    minimum_index = None
    minimum_length = 1000
    if all_paths == []:
        print('NO')
    else:
        for i in range(len(all_paths)):
            if getLength(all_paths[i], length_data) < minimum_length:
                minimum_length = getLength(all_paths[i], length_data)
                minimum_index = i
        for i in range(len(all_paths[minimum_index])):
            print(all_paths[minimum_index][i], end=' ')
            if all_paths[minimum_index][i] in rest_data:
                visited_rest.append(all_paths[minimum_index][i])
        print()
        visited_rest = sorted(visited_rest)
        if visited_rest == []:
            print('NO', end=' ')
        else:
            for i in visited_rest:
                print(i, end=' ')
        print(minimum_length)
    
def output2(all_paths, rest_data, length_data):
    most_rest = 0
    for i in range(len(all_paths)):
        count = 0
        for j in range(len(all_paths[i])):
            if all_paths[i][j] in rest_data:
                count += 1
        if count > most_rest:
            most_rest = count
    if most_rest == 0:
        print('NO')
    else:
        paths = []  # The most amounts of rest stops' path 
        for i in range(len(all_paths)):
            count = 0
            for j in range(len(all_paths[i])):
                if all_paths[i][j] in rest_data:
                    count += 1
            if count == most_rest:
                paths.append(all_paths[i])
        minimum_index = None
        minimum_length = 1000
        rest_visited = []
        for i in range(len(paths)):
            if getLength(paths[i], length_data) < minimum_length:
                minimum_length = getLength(paths[i], length_data)
                minimum_index = i
        for i in paths[minimum_index]:
            print(i, end=' ')
            if i in rest_data:
                rest_visited.append(i)
        print()
        rest_visited = sorted(rest_visited)
        for i in rest_visited:
            print(i, end=' ')
        print(minimum_length)    

if __name__ == '__main__':
    start, end, rest_data, graph, length_data = getData()
    all_paths = []
    getAllPaths_dfs(start, end, graph, [], [], all_paths)
    # print(all_paths)
    output1(all_paths, rest_data, length_data)
    output2(all_paths, rest_data, length_data)
