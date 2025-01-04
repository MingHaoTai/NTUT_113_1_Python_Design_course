# 2024-11-26
def getData():
    pack_no = input().split()
    load_limit = int(input())
    if load_limit < 1 or load_limit > 10:
        print('Input Error')
        return False
    for i in range(len(pack_no)-1):
        for j in range(i+1, len(pack_no)):
            if pack_no[i] == pack_no[j]:
                print('Duplicated ID')
                return False
    for i in range(len(pack_no)-1):
        if int(pack_no[i][0]) > load_limit:
            print('Load limit exceeded')
            return False
    compute(pack_no, load_limit)

def remove(data : list, bag : list):
    for i in bag:
        data.remove(i)
    return data

def compute(pack_no : list, load_limit : int):
    sum = 0
    for i in range(len(pack_no)):
        sum += int(pack_no[i][0])
    if sum % load_limit != 0:
        print('Cannot be delivered')
        return False
    N = sum // load_limit
    data = list([] for i in range(N))
    for i in range(N):
        bag = []
        if match(pack_no, load_limit, bag, 0) == False:
            return False
        # print(i)
        # print(bag)
        data[i].extend(bag)
        pack_no = remove(pack_no, bag)
    # print(data)
    output(data)

def output(data : list):
    new_data = list([] for i in range(len(data)))
    for i in range(len(data)):
        for j in range(len(data[i])):
            new_data[i].extend(data[i][j][1])
        new_data[i] = sorted(new_data[i])
    new_data = mySort(new_data)
    # print(new_data)
    f(new_data, [], 1)

def f(new_data : list, y : list, length : int):
    i = 0
    while True:
        # print(i)
        if i < len(new_data) and len(new_data[i]) == length :
            i += 1
            continue
        x = new_data[0:i]
        x.sort()
        y.extend(x)
        # print(y)
        if i == len(new_data):
            break
        else:
            f(new_data[i:], y, length+1)
        return
    print(len(y))
    for i in range(len(y)):
        for j in range(len(y[i])):
            print(y[i][j], end=' ')
        print()
    
def mySort(data : list):
    for i in range(len(data)-1):
        if len(data[i]) > len(data[i+1]):
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            mySort(data)
            break
    return data

def match(pack_no : list, load_limit : int, bag : list, index : int):   # Find bag
    if index >= len(pack_no):
        return False
    elif int(pack_no[index][0]) > load_limit:
        print('Cannot be delivered')
        return False 
    elif match(pack_no, load_limit, bag, index+1) == True:
        return True
    elif int(pack_no[index][0]) == load_limit:
        bag.append(pack_no[index])
        # print(bag)
        return True
    elif match(pack_no, load_limit - int(pack_no[index][0]), bag, index+1) == True:
        bag.append(pack_no[index])
        # print(bag)
        return True
    

getData()