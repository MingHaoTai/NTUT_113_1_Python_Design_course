def getData():
    all_goods = list(input().split())
    truck_limit = int(input())
    if truck_limit < 1 or truck_limit > 10:
        print('Input Error')
        return False
    check_name = [all_goods[0]]
    for i in range(1, len(all_goods)):
        if all_goods[i] not in check_name:
            check_name.append(all_goods[i])
        else:
            print('Duplicated ID')
            return False
    for i in all_goods:
        if int(i[0]) > truck_limit:
            print('Load limit exceeded')
            return False
    compute(all_goods, truck_limit)

def remove(data, bag):  # remove all elements of bag 
    for i in bag:
        data.remove(i)
    return data
    
def compute(all_goods, truck_limit):
    sum = 0
    for i in all_goods:
        sum += int(i[0])
    if sum % truck_limit != 0:
        print('Cannot be delivered')
        return False
    N = sum // truck_limit
    data = list([] for i in range(N))
    for i in range(N):
        bag = []
        if match(all_goods, truck_limit, bag, 0) == False:
            return False
        data[i].extend(bag)
        all_goods = remove(all_goods, bag)
    print(N)
    output(data)

def output(data):
    data = sorted(data, key=lambda x : len(x))
    for i in range(len(data)):
        data[i] = sorted(data[i], key=lambda x : x[1])
    length = len(data[0])
    index = 0
    for i in range(len(data)):
        if len(data[i]) > length or i == len(data)-1:
            if index == i:
                data[index:i+1] = sorted(data[index:i+1], key=lambda x : x[1])
            else:
                data[index:i] = sorted(data[index:i], key=lambda x : x[0][1])
            index = i
            length = len(data[i])
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j][1], end=' ')
        print()

def match(all_goods, truck_limit, bag, index):
    if index >= len(all_goods):
        return False
    elif int(all_goods[index][0]) > truck_limit:
        print('Cannot be delivered')
        return False
    elif int(all_goods[index][0]) == truck_limit:
        bag.append(all_goods[index])
        return True
    elif match(all_goods, truck_limit, bag, index+1) == True:
        return True
    elif match(all_goods, truck_limit - int(all_goods[index][0]), bag, index+1) == True:
        bag.append(all_goods[index])
        return True

getData()