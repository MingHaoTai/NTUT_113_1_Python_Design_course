# 2024-12-21
def getData():
    n, start, end = input().split()
    restStop = input().split()
    path = list(None for i in range(int(n)))
    for i in range(int(n)):
        path[i] = input().split()
    return start, end, restStop, path

def findAllPath(start : str, end : str, index : int, path : list, findPath : list):
    findPath.append([])
    i = 0
    while i < len(path):
        if start in path[i]:
            findPath[index].append(path[i])
            path.remove(path[i])
            i = 0
        else:
            i += 1
    for i in range(len(findPath[index])):
        if start in findPath[index][i]:
            findAllPath(findPath[index][i][findPath[index][i].index(start)-1], end, index+1, path, findPath) 

def allCorrect(start : str, end : str, findPath : list, index : int, bag : list):
    flag = False
    if index >= len(findPath):
        return False
    else:
        for i in range(len(findPath[index])):
            if start in findPath[index][i]:
                flag = True
                bag.append(findPath[index][i])
                if end in findPath[index][i]:
                    # print(bag)
                    bag = []
                    return True
                else:
                    if allCorrect(findPath[index][i][findPath[index][i].index(start)-1], end, findPath, index+1, bag) == True:
                        return True
        if flag == False:
            return False

if __name__ == '__main__':
    start, end, restStop, path = getData()
    findPath = []
    findAllPath(start, end, 0, path, findPath)
    i = 0
    while i < len(findPath):
        if findPath[i] == []:
            findPath.remove([])
            i = 0
        else:
            i += 1
    print(findPath)
    bag = []
    mul = 1
    for i in range(len(findPath)):
        mul = mul * len(findPath[i])
    for i in range(mul):
        bag = []
        allCorrect(start, end, findPath, 0, bag)
        print(bag)
    # data = [['1', '2'], ['3', '4']]
    # print('1' in data)
    # print(len([]))