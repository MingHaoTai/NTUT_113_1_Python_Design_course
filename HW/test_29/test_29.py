# 2024-12-02

def getData():
    s = input()
    n = int(input())
    return s, n

def permutation(s : str, current : str, data : list, length : int):
    if len(current) == length:
        data.append(current)
        return 
    for i in range(len(s)):
        a = s[i]
        b = permutation(s[0:i]+s[i+1:], current+a, data, length)
    return

def combination(s : str, data : list, n : int, count : int):
    count -= 1
    b = bin(count)[2:]
    b = b.zfill(len(s))
    # print(b)
    count_1 = 0
    current = ''
    if count == 0:
        return
    for i in range(len(b)):
        if b[i] == '1':
            count_1 += 1
            # print(b[i], count_1)
    if count_1 != n:
        return combination(s, data, n, count)
    else:
        # print(b)
        for i in range(len(b)):
            if b[i] == '1':
                current += s[i]
        data.append(current)
        # print(current)
        combination(s, data, n, count)

if __name__ == '__main__':
    s, n = getData()
    data = []
    permutation(s, '', data, len(s))
    for i in range(len(data)):
        if i == len(data)-1:
            print(data[i])
        else:
            print(data[i], end=', ')
    data = []
    combination(s, data, n, 2 ** len(s))
    for i in range(len(data)):
        if i == len(data)-1:
            print(data[i])
        else:
            print(data[i], end=', ')
    