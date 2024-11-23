# 2024-11-21
# 4*4 sudoku

def getSudoku():
    data = list(None for i in range(4))
    zero_index = []
    for i in range(4):
        data[i] = input().split()
    for i in range(4):
        for j in range(4):
            if data[i][j] == '0':
                zero_index.append([i, j]) 
    compute(data, zero_index)

def inputNum(data : list):
    if '1' not in data:
        return '1'
    elif '2' not in data:
        return '2'
    elif '3' not in data:
        return '3'
    elif '4' not in data:
        return '4'
    
def outputData(data : list):
    for i in range(4):
        for j in range(4):
            print(data[i][j], end=' ')
        print()

def compute(data : list, zero_index : list): 
    flag = True
    if zero_index == []:
        outputData(data)
        return True 
    for x in range(len(zero_index)):
        count = 0
        if flag == True:
            bag = []
            for j in range(4):
                bag.append(data[zero_index[x][0]][j])
                if data[zero_index[x][0]][j] == '0':
                    count += 1
                if count > 1:
                    count = 0
                    break
            if count == 1:
                flag = False
                ans = inputNum(bag)
                data[zero_index[x][0]][bag.index('0')] = ans 
                zero_index.remove(zero_index[x])

        if flag == True:
            bag = []
            for i in range(4):
                bag.append(data[i][zero_index[x][1]])
                if data[i][zero_index[x][1]] == '0':
                    count += 1
                if count > 1:
                    count = 0
                    break
            if count == 1:
                flag = False
                ans = inputNum(bag)
                data[bag.index('0')][zero_index[x][1]] = ans
                zero_index.remove(zero_index[x])
        
        if flag == True:
            bag = []
            i_start = (zero_index[x][0] // 2) * 2
            j_start = (zero_index[x][1] // 2) * 2
            for i in range(i_start, i_start + 2):
                for j in range(j_start, j_start + 2):
                    bag.append(data[i][j])
                    if data[i][j] == '0':
                        count += 1
                if count > 1:
                    count = 0
                    break
            if count == 1:
                flag = False
                ans = inputNum(bag)           
                data[i_start + (bag.index('0') // 2)][j_start + (bag.index('0') % 2)] = ans
                zero_index.remove(zero_index[x])
        
        if flag == False:
            break
    compute(data, zero_index)

getSudoku()