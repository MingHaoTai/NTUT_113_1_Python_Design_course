# 2024-12-01
def getData():
    n = int(input())
    m = int(input())
    a = input().split()
    b = input().split()
    circle = input().split()
    return n, m, a, b, circle

def getMatrix(data : list, n : int):
    newData = list([None]*n for i in range(n))
    count = 0
    for i in range(n):
        for j in range(n):
            newData[i][j] = data[count]
            count += 1
    return newData

def matchStraight(data : list, circle : list):
    score = 0
    for i in range(len(data)):
        row = 0
        for j in range(len(data)):
            if data[i][j] in circle:
                row += 1
        if row == len(data):
            score += 1
    for i in range(len(data)):
        col = 0
        for j in range(len(data)):
            if data[j][i] in circle:
                col += 1
        if col == len(data):
            score += 1
    return score

def matchDiagonal(data : list, circle : list):
    score = 0
    count = 0
    for i in range(len(data)):
        if data[i][i] in circle:
            count += 1
    if count == len(data):
        score += 1
    count = 0
    for i in range(len(data)-1, -1, -1):
        if data[len(data)-i-1][i] in circle:
            count += 1
    if count == len(data):
        score += 1
    return score

if __name__ == '__main__':
    n, m, a, b, circle = getData()
    a, b = getMatrix(a, n), getMatrix(b, n)
    score_a = matchDiagonal(a, circle) + matchStraight(a, circle)
    score_b = matchDiagonal(b, circle) + matchStraight(b, circle)
    if score_a > score_b:
        print('A win')
    elif score_a < score_b:
        print('B win')
    else:
        print('Tie')
    