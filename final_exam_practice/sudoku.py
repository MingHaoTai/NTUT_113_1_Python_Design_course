def getData():
    data = list(None for i in range(4))
    for i in range(4):
        data[i] = list(map(int, input().split()))
    return data

def compute(data : list):
    for i in range(len(data)):
        if 0 in data[i]:
            break
        elif 0 not in data[i] and i == len(data) - 1:
            return 

    index = [0, 0]
    for i in range(len(data)):  # Find in every row
        count = 0
        for j in range(len(data)):
            if data[i][j] == 0:
                index = [i, j]
                count += 1
            if count > 1:
                index = [0, 0]
                break
        if count == 1:
            num = getNum(data[i])
            data[index[0]][index[1]] = num
    for i in range(len(data)):  # Find in every col
        count = 0
        for j in range(len(data)):
            if data[j][i] == 0:
                index = [j, i]
                count += 1
            if count > 1:
                index = [0, 0]
                break
        if count == 1:
            num = getNum([data[0][i], data[1][i], data[2][i], data[3][i]])
            data[index[0]][index[1]] = num
    for i in range(0, 4, 2):  # Find in every square 
        for j in range(0, 4, 2):
            count = 0
            square = [data[i][j], data[i][j+1], data[i+1][j], data[i+1][j+1]]
            for a in range(4):
                if square[a] == 0:
                    if a < 2:
                        index = [i, j + a] 
                    else:
                        index = [i + 1, j + a - 2]
                    count += 1
                if count > 1:
                    index = [0, 0]
                    break
            if count == 1:
                num = getNum(square)
                data[index[0]][index[1]] = num
    compute(data)
        
def getNum(data : list):
    if 1 not in data:
        return 1
    elif 2 not in data:
        return 2
    elif 3 not in data:
        return 3
    elif 4 not in data:
        return 4

def output(data : list):
    for i in data:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == '__main__':
    data = getData()
    compute(data)
    output(data)
