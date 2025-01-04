def getData():
    player = int(input())
    size = int(input())
    n = int(input())
    name = input().split()
    num = {}
    for i in range(player):
        num[name[i]] = list(map(int, input().split()))
    circle = list(map(int, input().split()))
    return num, circle, size

def getMatrix(data : list, size : int):
    matrix = list([] for i in range(size))
    for i in range(size):
        matrix[i] = data[i*size:i*size+size]
    return matrix

def checkRow(matrix : list, circle : list):
    score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] in circle and j == len(matrix)-1:
                score += 1
            elif matrix[i][j] not in circle:
                break
    return score

def checkCol(matrix : list, circle : list):
    score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] in circle and j == len(matrix)-1:
                score += 1
            elif matrix[j][i] not in circle:
                break
    return score

def checkLeftSlash(matrix : list, circle : list):
    for i in range(len(matrix)):
        if matrix[i][i] in circle and i == len(matrix)-1:
            return 1
        elif matrix[i][i] not in circle:
            return 0

def checkRightSlash(matrix : list, circle : list):
    for i in range(len(matrix)):
        if matrix[i][len(matrix)-i-1] in circle and i == len(matrix)-1:
            return 1
        elif matrix[i][len(matrix)-i-1] not in circle:
            return 0

def countScore(matrix : list, circle : list):
    score = 0
    score += checkRow(matrix, circle)
    score += checkCol(matrix, circle)
    score += checkLeftSlash(matrix, circle)
    score += checkRightSlash(matrix, circle)
    return score

def winner(score : dict):
    maxScore = 0
    winPlayer = {}
    for i in score:
        if score[i] > maxScore:
            maxScore = score[i]
    for i in score:
        if score[i] == maxScore:
            winPlayer[i] = score[i]
    return winPlayer

if __name__ == '__main__': 
    player, circle, size = getData() 
    score = {}
    for i in player:
        player[i] = getMatrix(player[i], size)
        score[i] = countScore(player[i], circle)
    winPlayer = winner(score)
    if len(winPlayer) == len(player):
        print('Tie ', end='')
        for i in player:
            print(i, end=' ')
        print(winPlayer[i])
    else:
        for i in winPlayer:
            print(i, end=' ')
        print(winPlayer[i])