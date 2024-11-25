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
    N = sum // load_limit
    data = list([] for i in range(N))
    for i in range(N):
        bag = []
        if match(pack_no, load_limit, bag, 0) == False:
            return False
        print(i)
        print(bag)
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
    print(new_data)
    x = []
    # while True:
    #     if len(data) == 0:
    #         break
    #     for i in range(len(data)-1):
    #         if len(data[i]) == len(data[i+1]):
    #             x = data[0:i+2]
    #         else:
    #             break
    #     x.sort()
    #     for i in range(len(x)):
    #         for j in range(len(x[i])):
    #             print(x[i][j], end=' ')    
    #         print()
    #         data.remove(x[i])
    
def mySort(data : list):
    for i in range(len(data)-1):
        if len(data[i]) > len(data[i+1]):
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp
            mySort(data)
            break
    return data

def match(pack_no : list, load_limit : int, bag : list, index : int):
    if index >= len(pack_no):
        return False
    elif int(pack_no[index][0]) > load_limit:
        print('Cannot be delivered')
        return False
    elif int(pack_no[index][0]) == load_limit:
        bag.append(pack_no[index])
        return True
    elif match(pack_no, load_limit, bag, index+1) == True:
        return True
    elif match(pack_no, load_limit - int(pack_no[index][0]), bag, index+1) == True:
        bag.append(pack_no[index])
        return True

getData()