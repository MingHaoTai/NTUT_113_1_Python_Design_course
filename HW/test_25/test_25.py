# 2024-11-24
def getBracketsInStr(s : str):
    brackets = ['(', '[', '{', ')', ']', '}']
    bracketsInString = []
    for i in range(len(s)):
        if s[i] in brackets:
            bracketsInString.append(s[i])
    return bracketsInString

def bracketsCheck(data : list, depth : int, max_depth : int):
    brackets = ['(', '[', '{', ')', ']', '}']
    for i in range(len(data)):
        if data[i] in brackets[0:3]:
            depth += 1
        elif data[i] in brackets[3:6] and brackets[brackets.index(data[i]) - 3] == data[i-1]:
            if depth > max_depth:
                max_depth = depth
            depth -= 1
            data.pop(i)
            data.pop(i-1)
            x = bracketsCheck(data, 0, max_depth)
            if x == 0:
                return 0
            else:
                max_depth = x
            break
        else:
            print('fail')
            return 0
    if data != []:
        print('fail')
        return 0
    else:
        return max_depth

def getNumInDepth(s : list, bracketsData : list, max_depth : int):
    brackets = ['(', '[', '{', ')', ']', '}']
    data = list([None] for i in range(7))
    j, depth = 0, 0
    for i in range(len(s)):
        if s[i] in brackets[0:3] and  s[i] == bracketsData[j]:
            j += 1 
            depth += 1
        elif s[i] in brackets[3:6] and s[i] == bracketsData[j]:
            j += 1
            depth -= 1
        elif s[i] in brackets and s[i] != brackets[j]:
            print('fail')
            return False
        elif s[i] not in brackets:
            data[depth].append(s[i])
    return data

def strToList(s : str):
    data = []
    for i in range(len(s)):
        data.append(s[i])
    return data

if __name__ == '__main__':
    strAmount = int(input())
    findDepth = int(input())
    data = []
    for i in range(strAmount):
        data.append(input())
    for i in range(strAmount):
        dataBrackets = getBracketsInStr(data[i])
        dataDepth = bracketsCheck(getBracketsInStr(data[i]), 0, 0)
        dataList = strToList(data[i])
        if dataDepth == 0:
            continue
        print('pass,', end='')
        numData = getNumInDepth(dataList, dataBrackets, dataDepth)
        if findDepth > dataDepth or numData[findDepth] == [None]:
            print('EMPTY')
        else:
            for i in range(1, len(numData[findDepth])):
                print(numData[findDepth][i], end='')
            print()
