#2024-11-04

def GetArray(n : int):
    if n < 1 or n > 10:
        print('ERROR')
        return
    count = 0
    Array = list([None]*n for i in range(n))
    if count < n*n:
        for row in range(n):
            for col in range(n):
                Array[row][col] = count
                count += 1
    return Array

def transpose(m : int, array : list):
    new_array = list([None]*len(array) for i in range(len(array)))
    if m == 0:
        return array
    elif m == 1:
        for row in range(len(array)):
            new_array[row] = array[len(array) - row - 1]
        return new_array
    else:
        for row in range(len(array)):
            for col in range(len(array)):
                new_array[row][col] = array[len(array) - col - 1][row]
        return new_array

def Output_Array(array : list):
    for i in range(len(array)):
        for j in range(len(array)):
            print(str(array[i][j]).rjust(3), end='')
        print()
    return

def main():
    n = int(input())
    array = GetArray(n)
    m = []

    while True:
        m_in = int(input())
        if m_in == -1:  # when m_in = -1 => STOP
            break
        m.append(m_in)

    for i in range(len(m)):
        if m[i] >= 0 and m[i] <= 2: # 0 <= m <= 2
            Output_Array(transpose(m[i], array))
        else:   # if m = -1 => ERROR
            print('ERROR')


if __name__ == '__main__':
    main()