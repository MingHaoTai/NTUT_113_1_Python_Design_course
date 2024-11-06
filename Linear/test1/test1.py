import math

A = [[2, -2], [3, -5]]
B = [[-2, 0], [0, 2]]
C = [[-1, 2, 0], [2, 0, 3]]
E = [[2, -1], [math.pi, math.log(2, 10)], [-2, 3]]
F = [[1, 2, 3], [2, 3, 4], [3, 5, 7]]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def Transpose(A : list):
    row = len(A)
    col = len(A[0])
    B = [[0]*row for a in range(col)]
    for i in range(0, row):
        for j in range(0, col):
            B[j][i] = A[i][j]
    return B

def Div_Const(A :list, const : int):
    row = len(A)
    col = len(A[0])
    for i in range(0, row):
        for j in range(0, col):
            A[i][j] = A[i][j] / const
    return A

def Mul_Const(A : list, const : int):
    row = len(A)
    col = len(A[0])
    for i in range(0, row):
        for j in range(0, col):
            A[i][j] = A[i][j] * const
    return A

def Mul_Two_Matrices(A : list, B : list):
    row_A = len(A)
    col_A = len(A[0])
    row_B = len(B)
    col_B = len(B[0])
    if col_A != row_B:
        print('ERROR:The first matrix col not equal to the second matrix row')
        return
    else:
        C = [[0]*col_B for a in range(row_A)]
        for i in range(0, row_A):
            for j in range(0, col_B):
                for x in range(0, col_A):
                    C[i][j] = C[i][j] + (A[i][x] * B[x][j])
        return C

def Add(A : list, B : list):
    row_A = len(A)
    col_A = len(A[0])
    row_B = len(B)
    col_B = len(B[0])
    if row_A != row_B or col_A != col_B:
        print('ERROR:two matrices are not the same size!')
        return
    else:
        C = [[0]*col_A for a in range(row_A)]
        for i in range(0, row_A):
            for j in range(0, col_A):
                C[i][j] = A[i][j] + B[i][j]
        return C

def Sub(A : list, B : list):
    row_A = len(A)
    col_A = len(A[0])
    row_B = len(B)
    col_B = len(B[0])
    if row_A != row_B or col_A != col_B:
        print('ERROR:two matrices are not the same size!')
        return
    else:
        C = [[0]*col_A for a in range(row_A)]
        for i in range(0, row_A):
            for j in range(0, col_A):
                C[i][j] = A[i][j] - B[i][j]
        return C

def Inverse(A : list):
    row = len(A)
    B = [[0]*2 for a in range(row)]
    if row == 2:
        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        if det == 0:
            print('The matrix is not invertible!')
            return
        else:
            B[0][0] = A[1][1]
            B[1][1] = A[0][0]
            B[0][1] = -A[0][1]
            B[1][0] = -A[1][0]
            B = Div_Const(B, det)
            return B
    elif row == 3:
        det = (A[0][0] * A[1][1] * A[2][2]) + (A[0][1] * A[1][2] * A[2][0]) + (A[0][2] * A[1][0] * A[2][1]) - (A[0][2] * A[1][1] * A[2][0]) - (A[0][1] * A[1][0] * A[2][2]) - (A[0][0] * A[1][2] * A[2][1])
        if det == 0:
            print('The matrix is not invertible!')
            return
        else:
            B[0][0] = A[1][1] * A[2][2] - A[1][2] * A[2][1]
            B[1][0] = -(A[1][0] * A[2][2] - A[1][2] * A[2][0])
            B[2][0] = A[1][0] * A[2][1] - A[1][1] * A[2][0]
            B[0][1] = -(A[0][1] * A[2][2] - A[0][2] * A[2][1])
            B[1][1] = A[0][0] * A[2][2] - A[0][2] * A[2][0]
            B[2][1] = -(A[0][0] * A[2][1] - A[0][1] * A[2][0])
            B[0][2] = A[0][1] * A[1][2] - A[0][2] * A[1][1]
            B[1][2] = -(A[0][0] * A[1][2] - A[0][2] * A[1][1])
            B[2][2] = A[0][0] * A[1][1] - A[0][1] * A[1][0]
            B = Div_Const(B, det)
            return B

def diagonal(A : list):
    row = len(A)
    col = len(A[0])
    if row != col:
        print('This is not a diagonal matrix!')
        return
    else:
        for i in range(0, row):
            for j in range(0, col):
                if i != j and A[i][j] != 0:
                    print('This is not a diagonal matrix!')
                    return
        print('This is a diagonal matrix!')

def symmetric(A : list):
    row = len(A)
    col = len(A[0])
    if row != col:
        print('This is not a symmetric matrix!')
        return
    else:
        B = Transpose(A)
        if A == B:
            print('This is a symmetric matrix!')
            return
        else:
            print('This is not a symmetric matrix!')
            return

def to_2f(A : list):
    if type(A) != list:
        return
    row = len(A)
    col = len(A[0])
    for i in range(0, row):
        for j in range(0, col):
            if type(A[i][j]) == float:
                A[i][j] = int(A[i][j] / 0.01)
                A[i][j] = float(A[i][j] / 100)
    return A

def main():
    while True:
        print()
        print('Please input the mod:')
        mod = input()
        match mod:
            case 'a':
                print('Please input NO(1.A+3B, 2.C-B*ET, 3.AT):')
                no = int(input())
                if no == 1:
                    sum = Add(A, Mul_Const(B, 3))
                    print('A+3B=' + str(to_2f(sum)))
                elif no == 2:
                    sum = Sub(C, Mul_Two_Matrices(B, Transpose(E)))
                    print('C-B*ET=' + str(to_2f(sum)))
                elif no == 3:
                    A_T = Transpose(A)
                    print('AT=' + str(to_2f(A_T)))
                continue
            case 'b':
                M = Mul_Two_Matrices(A, B)
                N = Mul_Two_Matrices(B, A)
                if M == N:
                    print('M=A*B, N=B*A => M=N')
                else:
                    print('M=A*B, N=B*A => M!=N')
                continue
            case 'c':
                P = Mul_Two_Matrices(Transpose(C), Transpose(B))
                Q = Transpose(Mul_Two_Matrices(B, C))
                if P == Q:
                    print('P=CT*BT, Q=(B*C)T => P=Q')
                else:
                    print('P=CT*BT, Q=(B*C)T => P!=Q')
                continue
            case 'd':
                print('Please input NO(1.A, 2.F):')
                no = int(input())
                if no == 1:
                    print('Inverse of A:' + str(to_2f(Inverse(A))))
                elif no == 2:
                    print('Inverse of F:' + str(to_2f(Inverse(F))))
                continue
            case 'e':
                print('Please input NO(1.A, 2.B, 3.F, 4.I):')
                no = int(input())
                if no == 1:
                    diagonal(A)
                elif no == 2:
                    diagonal(B)
                elif no == 3:
                    diagonal(F)
                elif no == 4:
                    diagonal(I)
                continue
            case 'f':
                print('Please input NO(1.A, 2.B, 3.F, 4.I):')
                no = int(input())
                if no == 1:
                    symmetric(A)
                elif no == 2:
                    symmetric(B)
                elif no == 3:
                    symmetric(F)
                elif no == 4:
                    symmetric(I)
                continue
            case 'end':
                break

if __name__ == '__main__':
    main()