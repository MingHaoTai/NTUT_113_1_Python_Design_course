# 2024-12-26
import math

def chooseMatrix():
    matrix = {'a' : [[1, 6], [5, 2]], 'b' : [[2, 3], [3, -6]], 'c' : [[7, 2], [-4, 1]], 'x' : [[1, 1], [-1, 1]], 'z' : [[0, 0], [0, 0]]}
    no = input('no(ex:a, b, c, x, z): ')
    if no not in matrix:
        print('Please input legal no!')
        return False
    else:
        return matrix[no]

def getDeterminant(matrix : list):
    determinant = list([None] * 2 for i in range(2))
    for i in range(2):
        for j in range(2):
            if i == j:
                determinant[i][j] = str(matrix[i][j]) + '-l'
            else:
                determinant[i][j] = str(matrix[i][j])
    return determinant

def findEigenvalues(matrix : list):   
    if matrix == [[0, 0], [0, 0]]:
        print('This matrix dos not have any eigenvalues!')
        return 0, 0
    determinant = getDeterminant(matrix)
    elem = []
    for i in range(2):
        for j in range(2):
            elem.append(determinant[i][j])
    elem = [elem[0], elem[3], elem[1], elem[2]]
    x = []
    l = int(elem[0][0:len(elem[0])-2]) * int(elem[1][0:len(elem[1])-2]) - int(elem[2])*int(elem[3])
    x.append(l)
    l = -(int(elem[0][0:len(elem[0])-2]) + int(elem[1][0:len(elem[1])-2]))
    x.append(l)
    x.append(1)
    x1, x2 = solveEquation(x)
    return x1, x2

def solveEquation(equ : list):
    discriminant = equ[1] ** 2 - 4 * equ[0] * equ [2]
    x1, x2 = 0, 0
    if discriminant == 0:
        x1 = int(-equ[1] / (2 * equ[2]))
        print(f'This matrix just has one eigenvalue : {x1}')
    elif discriminant > 0:
        x1 = int((-equ[1] + math.sqrt(discriminant)) / (2 * equ[2]))
        x2 = int((-equ[1] - math.sqrt(discriminant)) / (2 * equ[2]))
        print(f'This has two eigenvalues : {x1}, {x2}')
    else:
        real_part = -equ[1] / (2 * equ[2])
        imaginary_part = (abs(discriminant)**0.5) / (2 * equ[2])
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        print(f"This matrix has two eigenvalues of imaginary number : {x1}, {x2}")
    return x1, x2

def findEigenvectors(matrix : list, x : list):
    augmented = list([0, 0, 0] for i in range(2))
    for i in x:
        for a in range(2):
            for b in range(2):
                if a == b:
                    augmented[a][b] = int(matrix[a][b]) - int(i)
                else:
                    augmented[a][b] = int(matrix[a][b])
        equ = solve_augmented_matrix(augmented)
        equ = [i * 10 for i in equ]
        a, b = int(equ[0]), int(equ[1])
        while b != 0:
            a, b = b, a % b
        if a == 1 or a == -1:
            flag = False
        else:
            flag = True
            equ[0] = int(equ[0] // a)
            equ[1] = int(equ[1] // a)
        x = [0, 0]
        if flag == False:
            if equ[0] == equ[1]:
                x = [1, -1]
            elif equ[0] == - equ[1]:
                x = [1, 1]
            else:
                x = [int(equ[1]*100)/100, -int(equ[0]*100)/100]
        else:
            x = [int(equ[1]*100)/100, -int(equ[0]*100)/100]
        print(f'The vector of the eigenvectors corresponding to {i} : {x}')

def solve_augmented_matrix(matrix : list):
    rows, cols = len(matrix), len(matrix[0])
    pivot_row = 0
    for col in range(cols - 1):
        for row in range(pivot_row, rows):
            if matrix[row][col] != 0:
                matrix[pivot_row], matrix[row] = matrix[row], matrix[pivot_row]
                break
        else:
            continue
        pivot = matrix[pivot_row][col]
        matrix[pivot_row] = [element / pivot for element in matrix[pivot_row]]
        for row in range(rows):
            if row != pivot_row and matrix[row][col] != 0:
                factor = matrix[row][col]
                matrix[row] = [matrix[row][i] - factor * matrix[pivot_row][i] for i in range(cols)]
        pivot_row += 1
    return matrix[0][0:2]

if __name__ == '__main__':
    matrix = chooseMatrix()
    if matrix != False:
        x1, x2 = findEigenvalues(matrix)
        if type(x1) == int and x1 != 0 and x2 != 0:
            x = [x1, x2]
            findEigenvectors(matrix, x)