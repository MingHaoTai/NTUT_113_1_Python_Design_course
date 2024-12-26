from collections import defaultdict, deque

def find_shortest_path(N, X, Z, rest_points, roads):
    # 建立部落圖的鄰接表
    graph = defaultdict(list)
    for A, B in roads:
        graph[A].append(B)
        graph[B].append(A)

    # 定義 BFS 搜尋
    def bfs(start, target, must_visit):
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            current, path = queue.popleft()
            if current == target and must_visit.issubset(path):
                return path
            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return None

    # 找從 X 經過某個休息點到 Z 的最短路徑
    shortest_path = None
    shortest_rest_point = None
    for rest_point in rest_points:
        path = bfs(X, Z, {rest_point})
        if path and (shortest_path is None or len(path) < len(shortest_path)):
            shortest_path = path
            shortest_rest_point = rest_point

    return shortest_rest_point, shortest_path

# 輸入處理
if __name__ == "__main__":
    # 第一行輸入
    first_line = input().strip().split()
    N, X, Z = map(int, first_line)

    # 第二行輸入
    rest_points = set(map(int, input().strip().split()))

    # 第三行到第 N+2 行輸入
    roads = []
    for _ in range(N):
        A, B = map(int, input().strip().split())
        roads.append((A, B))

    # 計算結果
    rest_point, path = find_shortest_path(N, X, Z, rest_points, roads)

    # 輸出結果
    if path:
        print(rest_point)
        print(" ".join(map(str, path)))
    else:
        print("NO")