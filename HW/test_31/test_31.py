# 2024-12-08
def permutation(data : list, perData : list, current : str, n : int):
    if len(current) == n:
        perData.append(current)
        return
    for i in data:
        if i not in current:
            permutation(data, perData, current + i, n)

def hexToDec(h : str):
    d = 0
    h_data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    d_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15]
    for i in range(len(h)):
        x = d_data[h_data.index(h[i])]
        d += 16**(len(h)-i-1)*x
    return d

def getSum(n : int):
    count = 0
    for i in range(len(str(n))):
        count += int(str(n)[i])
    return count

if __name__ == '__main__':
    inData = input().split()
    perData = []
    inData.sort()
    permutation(inData, perData, '', len(inData))
    if len(perData) % 2 == 0:
        ave = (hexToDec(perData[len(perData)//2]) + hexToDec(perData[len(perData)//2 - 1]))//2
    else:
        ave = hexToDec(perData[len(perData)//2])
    n = hexToDec(perData[0]) + hexToDec(perData[len(perData)-1]) + ave
    while n >= 10:
        n = getSum(n)
    print(n)
    